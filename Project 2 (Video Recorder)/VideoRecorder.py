import os
import cv2
import streamlit as st
import moviepy.editor as mp

st.title("Video Recording App")
text=st.text_input("Enter filename....")
st.sidebar.title("Video Recordings")
# Start Button Recording
if st.button("Start Recording"):
    if len(text)!=0:

        cap = cv2.VideoCapture(0)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Video download in Videos Folder
        writer = cv2.VideoWriter('Videos/TempVideo.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (width, height))

        while True:
            ret, frame = cap.read()

            writer.write(frame)

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        writer.release()
        cv2.destroyAllWindows()

        clip = mp.VideoFileClip("Videos/TempVideo.avi")
        path = "Videos/"+text+".mp4"
        a = clip.write_videofile(path)
        os.remove("Videos/TempVideo.avi")
        if a is None:
            st.write("Done")
        os.system("streamlit run VideoRecorder.py")
    else:
        st.error("Please enter a File name")


# Sidebar

folder_path = "Videos"
files = os.listdir(folder_path)
if len(files) > 0:
    selected_files = st.sidebar.selectbox("Select a file", files)
    if st.sidebar.button("Play Video"):
        f = open(folder_path + "/" + selected_files, "rb")
        video_bytes = f.read()
        st.video(video_bytes)
        st.write(selected_files)
    if st.sidebar.button("Delete"):
        os.remove("Videos/" + selected_files)
        st.experimental_rerun()
else:
    st.sidebar.write("No Video Recordings")

# To hide Footer
hide_footer_style = """
   <style>
   .reportview-container .main footer {visibility: hidden;}    
   """
st.markdown(hide_footer_style, unsafe_allow_html=True)


