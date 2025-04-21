import os

def bulk_rename_files():
    print("=== FILE RENAMER 3000 (ADHD EDITION) ===")
    
    # Step 1: Ask for folder path
    folder_path = input("📂 Drag & drop your folder here: ").strip('"')
    
    # Step 2: Ask for renaming rules
    print("\n🛠 What do you want to do?")
    print("1. Add text to start")
    print("2. Add text to end")
    print("3. Replace text")
    print("4. Remove text")
    choice = input("Choose (1-4): ")
    
    # Step 3: Get details based on choice
    if choice == "1":
        text = input("Text to add at START: ")
        def new_name(old): return text + old
    elif choice == "2":
        text = input("Text to add at END (before extension): ")
        def new_name(old): return os.path.splitext(old)[0] + text + os.path.splitext(old)[1]
    elif choice == "3":
        old_text = input("Text to REPLACE: ")
        new_text = input("Replace with: ")
        def new_name(old): return old.replace(old_text, new_text)
    elif choice == "4":
        remove_text = input("Text to REMOVE: ")
        def new_name(old): return old.replace(remove_text, "")
    else:
        print("❌ Invalid choice!")
        return
    
    # Step 4: Preview changes
    print("\n🔍 PREVIEW (Old → New):")
    files = os.listdir(folder_path)
    for filename in files:
        print(f"{filename} → {new_name(filename)}")
    
    # Step 5: Confirm and rename
    confirm = input("\n🚀 Proceed? (y/n): ").lower()
    if confirm == "y":
        for filename in files:
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name(filename))
            os.rename(old_path, new_path)
        print("✅ Done! Files renamed.")
    else:
        print("❌ Cancelled.")

# Run the function
bulk_rename_files()
