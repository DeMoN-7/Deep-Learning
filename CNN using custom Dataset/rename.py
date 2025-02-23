import os

def rename_images(directory):
    files = sorted([f for f in os.listdir(directory) if f.lower().endswith(('jpg', 'jpeg', 'png'))])
    
    for i, filename in enumerate(files, start=1):
        ext = filename.split('.')[-1]  # Get file extension
        new_name = f"img{i}.{ext}"
        new_path = os.path.join(directory, new_name)

        # Ensure the new file name does not already exist
        count = 1
        while os.path.exists(new_path):
            new_name = f"img{i}_{count}.{ext}"
            new_path = os.path.join(directory, new_name)
            count += 1

        old_path = os.path.join(directory, filename)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

# Example usage
directory = r"D:\Mca_upes\Sem-2\Deep-Learning\CNN using custom Dataset\dataset\car"  # Update the path
rename_images(directory)
