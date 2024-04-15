import boto3


def extract_text_from_image(image_path):
    # Initialize the Textract client
    textract_client = boto3.client('textract')

    # Read the image as bytes
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    response = textract_client.detect_document_text(Document={'Bytes': image_bytes})

    # Extract text from the response
    extracted_text = ""
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            extracted_text += item["Text"] + "\n"

    return extracted_text


# # Replace 'image_path' with the path to your image file
# image_path = 'text_image.png'
# extracted_text = extract_text_from_image(image_path)
# print(extracted_text)
