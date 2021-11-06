import io
import os
from google.cloud import vision

# Imports the Google Cloud client library


# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('arabian4.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print (response)

Leopard_score=0
BigCats_score=0
Cheetah_score=0
Jaguar_score=0

print('Labels:')

for label in labels:  
    if label.description=="Leopard":
        Leopard_score = label.score
        Leopard_description = label.description
        
    if label.description=="Big cats":
        BigCats_score = label.score
        BigCats_description = label.description
        
    if label.description=="Cheetah":
        Cheetah_score = label.score
        Cheetah_description = label.description
       
    if label.description=="Jaguar":
        Jaguar_score = label.score
        Jaguar_description = label.description
        

if Leopard_score !=0:
    print(Leopard_description)
    print(Leopard_score)


elif Cheetah_score !=0:
    print(Cheetah_description)
    print(Cheetah_score)

elif BigCats_score !=0:
    print(BigCats_description)
    print(BigCats_score)

elif Jaguar_score !=0:
    print(Jaguar_score)
    print(Jaguar_description)

else:
    print("The leopard was not found")