import streamlit as st
from pptx import Presentation
from io import BytesIO
from PIL import Image
import tempfile

# タイトル設定
st.title("PPTX Viewer with Notes")

# ファイルアップロード
uploaded_file = st.file_uploader("Upload a PPTX file", type="pptx")

if uploaded_file is not None:
    # Presentationを読み込む
    presentation = Presentation(uploaded_file)
    
    # スライドとメモの保存用リスト
    slides = []
    notes = []
    
    # スライドとメモの取得
    for slide in presentation.slides:
        # スライド画像の作成（仮の画像としてテキストを含むサムネイル作成）
        img = Image.new('RGB', (720, 540), color='white')
        slides.append(img)
        
        # メモの取得
        note = slide.notes_slide.notes_text_frame.text if slide.has_notes_slide else "No notes available"
        notes.append(note)
    
    # スライドとメモの表示
    for i, (slide_img, note) in enumerate(zip(slides, notes)):
        st.image(slide_img, caption=f"Slide {i+1}")
        st.write("**Notes:**")
        st.write(note)
        st.markdown("---")