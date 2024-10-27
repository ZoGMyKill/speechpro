import tempfile

def save_uploaded_video(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False) as temp_video:
        temp_video.write(uploaded_file.read())
        return temp_video.name
