from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeAudioClip, AudioFileClip
from moviepy.video.fx.speedx import speedx  # นำเข้า speedx จาก moviepy.video.fx.speedx

class VideoEditor:
    def __init__(self, fps=30, resolution=(1280, 720)):
        self.video_path = None
        self.video_clip = None
        self.timeline_clips = []
        self.clip_start = 0
        self.clip_end = None
        self.final_clip = None
        self.fps = fps
        self.resolution = resolution
        self.bgm = None

    def open_video(self, path):
        """
        เปิดวิดีโอจาก path ที่กำหนด และเก็บวิดีโอไว้ในตัวแปร video_clip

        Parameters:
            path (str): ที่อยู่ของไฟล์วิดีโอที่จะเปิด
        """
        self.video_path = path
        self.video_clip = VideoFileClip(self.video_path)
        self.video_clip = self.video_clip.resize(self.resolution)


    def set_trim(self, start_time, end_time):
        """
        กำหนดเวลาเริ่มต้นและสิ้นสุดของการตัดวิดีโอ

        Parameters:
            start_time (float): เวลาเริ่มต้นในการตัดวิดีโอ (หน่วยเป็นวินาที)
            end_time (float): เวลาสิ้นสุดในการตัดวิดีโอ (หน่วยเป็นวินาที)
        """
        if self.video_clip:
            self.clip_start = start_time
            self.clip_end = end_time

    def cut_clip(self):
        """
        ตัดวิดีโอตามเวลาเริ่มต้นและสิ้นสุดที่กำหนดไว้

        Returns:
            cut_clip (VideoFileClip): คลิปวิดีโอที่ถูกตัด
        """
        if self.video_clip and self.clip_end is not None:
            self.video_clip = self.video_clip.subclip(self.clip_start, self.clip_end)
            # self.timeline_clips.append(cut_clip)
            self.clip_start = 0
            self.clip_end = None

    def add_to_timeline(self, speed=1.0, text=""):
        """
        เพิ่มคลิปวิดีโอปัจจุบันไปยัง timeline พร้อมปรับความเร็วและข้อความ

        Parameters:
            speed (float): ความเร็วของคลิปวิดีโอ
            text (str): ข้อความที่จะแสดงบนคลิปวิดีโอ
        """
        if self.video_clip:
            if text:
                txt_clip = TextClip(text, fontsize=24, color='white').set_position('center').set_duration(self.video_clip.duration)
                video_with_text = CompositeAudioClip([self.video_clip, txt_clip])
                video_with_text = speedx(video_with_text, speed)  # เรียกใช้ speedx โดยตรง
                self.timeline_clips.append(video_with_text)
            else:
                clip_with_speed = speedx(self.video_clip, speed)  # เรียกใช้ speedx โดยตรง
                self.timeline_clips.append(clip_with_speed)

    def export_video(self, export_path):
        """
        ส่งออกวิดีโอไปยัง path ที่กำหนด

        Parameters:
            export_path (str): ที่อยู่ของไฟล์วิดีโอที่จะบันทึก
        """
        if self.timeline_clips:
            self.final_clip.write_videofile(export_path, codec='libx264', fps=self.fps)  # เพิ่ม codec 'libx264'
        else:
            raise ValueError("No clips in the timeline!")

    def merge_clips(self):
        """
        รวมคลิปใน timeline ทั้งหมดเป็นวิดีโอคลิปเดียว

        Returns:
            final_clip (VideoFileClip): วิดีโอที่รวมจากทุกคลิปใน timeline
        """
        if self.timeline_clips:
            self.final_clip = concatenate_videoclips(self.timeline_clips)
        else:
            raise ValueError("No clips in the timeline to merge!")

    def set_bgm(self, bgm_path):
        """
        กำหนดเสียงพื้นหลังของวิดีโอ

        Parameters:
            bgm_path (str): ที่อยู่ของไฟล์เสียงที่จะใช้เป็นเสียงพื้นหลัง
        """
        if self.final_clip:
            self.bgm = AudioFileClip(bgm_path)
            self.bgm = self.bgm.subclip(0, self.final_clip.duration)
            # bgm = CompositeAudioClip([self.final_clip.audio, bgm])
            # self.final_clip = self.final_clip.set_audio(bgm)

    def change_bgmvolume(self, volume=0.05):
        """
        ทดสอบการตั้งระดับเสียงของเสียงพื้นหลัง

        Parameters:
            volume (float): ระดับเสียงของเสียงพื้นหลัง
        """
        if self.final_clip:
            self.bgm = self.bgm.volumex(volume)

    def add_bgm(self):
        """
        เพิ่มเสียงพื้นหลังลงในวิดีโอ

        Returns:
            final_clip (VideoFileClip): วิดีโอที่มีเสียงพื้นหลัง
        """
        if self.final_clip and self.bgm:
            bgm = CompositeAudioClip([self.final_clip.audio, self.bgm])
            self.final_clip = self.final_clip.set_audio(bgm)
        else:
            raise ValueError("No background music to add!")

    def chang_finalvolume(self, volume=0.05):
        """
        ทดสอบการตั้งระดับเสียงของวิดีโอที่ส่งออก

        Parameters:
            volume (float): ระดับเสียงของวิดีโอที่ส่งออก
        """
        if self.final_clip:
            self.final_clip = self.final_clip.volumex(volume)

if __name__ is "__main__":
    # สร้างอินสแตนซ์ของ VideoEditor
    editor = VideoEditor()

    # เปิดไฟล์วิดีโอที่ต้องการตัดต่อ
    editor.open_video("c.mp4")

    # ตั้งเวลาเริ่มต้นและสิ้นสุดของการตัดวิดีโอ
    editor.set_trim(0, 10)

    # ตัดคลิปวิดีโอระหว่างเวลาที่ตั้งไว้
    editor.cut_clip()

    # เพิ่มคลิปที่ตัดลงใน timeline โดยไม่มีการปรับแต่งความเร็วหรือข้อความ
    editor.add_to_timeline()

    # เปิดไฟล์วิดีโอที่ต้องการนำมาต่อกับของเดิม
    editor.open_video("b.mp4")

    editor.set_trim(0, 10)
    editor.cut_clip()

    editor.add_to_timeline()

    editor.merge_clips()

    # ai มารับ video ที่ตัดแล้ว
    editor.export_video("sample1.mp4")


    # กำหนดเสียงพื้นหลังของวิดีโอ
    editor.set_bgm("epic.mp3")
    editor.change_bgmvolume(0.15)
    editor.add_bgm()
    editor.chang_finalvolume()

    # ส่งออกคลิปที่รวมแล้วไปยังไฟล์ที่ต้องการ
    editor.export_video("sample1.mp4")