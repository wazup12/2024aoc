set -e

PADDED_DATE=$(date +%d)
UNPADDED_DATE=$(date +%-d)
SESSION_COOKIE="$1"

mkdir -p "./$PADDED_DATE"

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <session_cookie>"
  exit 1
fi

# Use get_input.sh to fetch input and save to input.txt in the folder
./get_input.sh ${UNPADDED_DATE} ${SESSION_COOKIE} > "./$PADDED_DATE/input.txt"

# Create the main.py file with the desired contents
cat <<EOF > "./$PADDED_DATE/main.py"
FILENAME = "input.txt"
IO_ERROR = -1

def get_file_contents(filename=FILENAME):
    with open(filename) as f:
        conts = f.read()
        return conts

if __name__ == "__main__":
    conts = get_file_contents()
    if not conts: exit(IO_ERROR)

		print(conts)
EOF

echo "Setup complete: folder './$PADDED_DATE' created with input.txt and main.py"

