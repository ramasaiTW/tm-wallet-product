if [ -n "$TM_ACCESS_TOKEN" ];
then
  AUTH_TOKEN="$TM_ACCESS_TOKEN"
else
  echo "Required '$TM_ACCESS_TOKEN' variable is missing!"
  exit 1
fi

if [ -n "$TM_CORE_API_URL" ];
then
  # shellcheck disable=SC2034
  CORE_API_URL="$TM_CORE_API_URL"
else
  echo "Required '$TM_CORE_API_URL' variable is missing!"
  exit 1
fi

CONTENTS="./library"
COMMON_MANIFEST="$CONTENTS/common_manifest.yaml"
PRODUCT_MANIFEST="$CONTENTS/wallet_manifest.yaml"
CLU_RUNNER=./configuration-layer-utilities/clu-darwin-amd64

echo "Running CLU validate on '${COMMON_MANIFEST}' and '${PRODUCT_MANIFEST}'..."

"$CLU_RUNNER" version

if "$CLU_RUNNER" validate "$COMMON_MANIFEST" && "$CLU_RUNNER" validate "$PRODUCT_MANIFEST";
then
  echo "Running CLU import on '${COMMON_MANIFEST}'..."
  "$CLU_RUNNER" import "$COMMON_MANIFEST" --activate-on-import --auth-token "$AUTH_TOKEN" --core-api "$CORE_API_URL"

  echo "Running CLU import on '${PRODUCT_MANIFEST}'..."
  "$CLU_RUNNER" import "$PRODUCT_MANIFEST" --activate-on-import --auth-token "$AUTH_TOKEN" --core-api "$CORE_API_URL"
fi