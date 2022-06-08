from businesslogic.wav_to_midi import WavToMidi


class Convert:

    def __int__(self):
        return

    @staticmethod
    def convert_file(source_file_name, target_file_name):
        WavToMidi.convert_file(source_file_name, target_file_name)
