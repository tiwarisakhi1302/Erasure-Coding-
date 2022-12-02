def list_out_files(user):
      import os
      dir_path="./media/"+user+'_encoded'
      for path in os.scandir(dir_path):
            if path.is_file():
                  print(path.name)
