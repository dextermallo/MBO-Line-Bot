RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo "Enter your ${GREEN}AWS Access Key ID${NC}:"
read aws_access_key_id
echo "Enter your ${GREEN}AWS Secret Access Key${NC}:"
read aws_secret_access_key

export AWS_ACCESS_KEY_ID=$aws_access_key_id
export AWS_SECRET_ACCESS_KEY=$aws_secret_access_key

