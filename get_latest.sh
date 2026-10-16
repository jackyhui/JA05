#!/bin/bash
# Get the newest lesson files from GitHub.
#
# Run it from Terminal:   cd ~/JA05   then   ./get_latest.sh
#
# If you changed any lesson files, they are copied into my_work/saved_<date>/
# first, so nothing you wrote is lost. Then your JA05 folder is made the same
# as the teacher's copy on GitHub. Files inside my_work/ are never touched.

cd "$(dirname "$0")" || exit 1

if ! git rev-parse --git-dir >/dev/null 2>&1; then
    echo "This is not the JA05 folder from GitHub. Ask your teacher."
    exit 1
fi

echo "Checking GitHub for new files..."
if ! git fetch -q origin main; then
    echo "Cannot reach GitHub. Check you are on the Wi-Fi, then try again."
    exit 1
fi

# Files you changed or committed, plus your own files that have the same name
# as a new file coming from GitHub.
base=$(git merge-base HEAD origin/main 2>/dev/null || git rev-parse HEAD)
changed=$(
    {
        git -c core.quotepath=off diff --name-only HEAD
        git -c core.quotepath=off diff --name-only "$base" HEAD
        git -c core.quotepath=off diff --name-only --diff-filter=A HEAD origin/main |
            while IFS= read -r f; do
                if [ -e "$f" ] && ! git ls-files --error-unmatch "$f" >/dev/null 2>&1; then
                    echo "$f"
                fi
            done
    } | sort -u
)

saved=0
if [ -n "$changed" ]; then
    save_dir="my_work/saved_$(date +%Y-%m-%d_%H%M)"
    while IFS= read -r f; do
        if [ -f "$f" ]; then
            mkdir -p "$save_dir/$(dirname "$f")"
            cp -p "$f" "$save_dir/$f"
            saved=$((saved + 1))
        fi
    done <<< "$changed"
fi

git checkout -q -f main 2>/dev/null
git reset -q --hard origin/main

echo ""
if [ "$saved" -gt 0 ]; then
    echo "You had changed $saved file(s). Your copies are safe in:"
    echo "    $save_dir"
    echo ""
fi
echo "Done. You have the latest files."
