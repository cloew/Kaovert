from kao_command import Commands

commands = Commands(__name__, {'audio':'list_audio_tracks.ListAudioTracks',
                               'subtitles':'list_subtitle_tracks.ListSubtitleTracks',
                               'config':'new_config.NewConfig',
                               'convert':'convert.Convert',
                               'presets':'list_presets.ListPresets',
                               'preview':'preview.Preview',
                               'add':{'audio':'add_audio.AddAudio',
                                      'subtitle':'add_subtitle.AddSubtitle'}})