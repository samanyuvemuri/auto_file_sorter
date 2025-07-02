import os, shutil

path = ''

file_name = os.listdir(path)

folder_names = ['JPEG Files', 'PowerPoint Presentations', 'Word Documents', 'PDF Documents', 'PNG Images']

for i in range(0,5):
  if not os.path.exists(path + folder_names[i]):
    os.makedirs((path + folder_names[i]))

for file in file_name:
  if (file.endswith((".jpeg", ".jpg", ".JPG"))) and (not os.path.exists(path + "JPEG Files/" + file)):
    shutil.move(path + file, path + "JPEG Files/" + file)
  if (file.endswith(".pptx")) and (not os.path.exists(path + "PowerPoint Presentations/" + file)):
    shutil.move(path + file, path + "PowerPoint Presentations/" + file)
  if (file.endswith(".docx")) and (not os.path.exists(path + "Word Documents/" + file)):
    shutil.move(path + file, path + "Word Documents/" + file)
  if (file.endswith((".pdf", ".PDF"))) and (not os.path.exists(path + "PDF Documents/" + file)):
    shutil.move(path + file, path + "PDF Documents/" + file)
  if (file.endswith(".png")) and (not os.path.exists(path + "PNG Images/" + file)):
    shutil.move(path + file, path + "PNG Images/" + file)