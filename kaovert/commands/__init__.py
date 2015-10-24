from kao_command import Commands

commands = Commands(__name__, {'audio':'list_audio_tracks.ListAudioTracks',
                               'subtitles':'list_subtitle_tracks.ListSubtitleTracks',
                               'config':'new_config.NewConfig'})