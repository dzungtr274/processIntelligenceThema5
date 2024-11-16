# Scene 01

Scene 01 recorded in the Solve4X dataset with 3 process instances.

Start: 2024-03-25 08:48:23  
End: 08:54:55 (0:06:32.066000)

This scene covers the following 3 process instances:


- [ID001](#id001): Asset disbursement to clients
- [ID002](#id002): Asset disbursement to clients
- [ID003](#id003): Asset disbursement to clients

The scene was systematically planned prior to recording. Any deviations in behavior are intentional. 
The overall `itam.ocelxml` event log remains consistent with what is captured on camera and annotated in the video logs. 

## Resource Overview

| Resource | Entity   |
|----------|----------|
| Humans   | A1, C1, C2, C6  |
| Assets   | L1, P2, M1, L2, P3  |



## ID001

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 08:48:32.113 | 08:48:37.040 | Enter room    | C1 |  | door |
| 2  | 08:48:39.585 | 08:48:48.719 | Chat    | A1, C1 |  | it_working_desk |
| 3  | 08:48:49.404 | 08:49:05.479 | Pick asset from warehouse    | A1 | L1 | laptop_shelf |
| 4  | 08:49:05.308 | 08:49:19.530 | Pick asset from warehouse    | A1 | P2 | mouse_cupboard |
| 5  | 08:49:22.000 | 08:49:45.972 | Check asset quality    | A1 | L1, P2 | it_working_desk |
| 6  | 08:49:54.429 | 08:50:47.448 | Check-Out asset to user    | A1 | L1, P2 | it_working_desk |
| 7  | 08:50:49.609 | 08:50:53.599 | Handover asset to user    | A1, C1 | L1, P2 | it_working_desk |
| 8  | 08:50:55.815 | 08:50:59.438 | Leave room    | C1 |  | door |

## ID002

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 08:51:18.935 | 08:51:23.073 | Enter room    | C2 |  | door |
| 2  | 08:51:26.176 | 08:51:33.435 | Chat    | A1, C2 |  | it_working_desk |
| 3  | 08:51:33.489 | 08:51:42.352 | Pick asset from warehouse    | A1 | M1 | monitor_storage |
| 4  | 08:51:42.352 | 08:52:02.216 | Check asset quality    | A1 | M1 | it_working_desk |
| 5  | 08:52:10.180 | 08:52:30.895 | Check-Out asset to user    | A1 | M1 | it_working_desk |
| 6  | 08:52:33.802 | 08:52:37.552 | Handover asset to user    | A1, C2 | M1 | it_working_desk |
| 7  | 08:52:40.897 | 08:52:47.625 | Leave room    | C2 |  | door |

## ID003

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 08:52:01.824 | 08:52:06.422 | Enter room    | C6 |  | door |
| 2  | 08:52:38.891 | 08:52:52.020 | Chat    | A1, C6 |  | it_working_desk |
| 3  | 08:52:52.020 | 08:53:08.440 | Pick asset from warehouse    | A1 | P3 | mouse_cupboard |
| 4  | 08:53:08.440 | 08:53:33.913 | Pick asset from warehouse    | A1 | L2 | laptop_shelf |
| 5  | 08:53:35.226 | 08:53:46.520 | Check asset quality    | A1 | L2, P3 | it_working_desk |
| 6  | 08:53:55.602 | 08:54:33.406 | Check-Out asset to user    | A1 | L2, P3 | it_working_desk |
| 7  | 08:54:36.487 | 08:54:46.870 | Handover asset to user    | A1, C6 | L2, P3 | it_working_desk |
| 8  | 08:54:52.178 | 08:54:55.833 | Leave room    | C6 |  | door |



## Scene Files

The files related to this scene are stored in `scene01/` as follows:

| Type                  | Filename                    |
|-----------------------|-----------------------------|
| Video                 | `scene01.mp4`      |
| Video Log             | `scene01_vid.json` |
| Joined Scene OCEL[^1] | `scene01_ocel.json` |
| Video OCEL            | `scene01_video_ocel.json` |
| Ambient Sensor OCEL   | `scene01_sensors_ocel.json` |
| Motion Tracking       | `scene01_mov.csv`|
| Web Task Mining       | `scene01_ui.csv` |
| Reed Switches         | `scene01_reed_switches.csv`  |
| Distance Sensor Laptop Shelf | `scene01_distance_sensor_laptop_shelf.csv`  |
| Room Temp and Humidity | `scene01_temp_hum_sensor_window.csv` |

### Video file metrics

```json
{
  "streams": [
    {
      "index": 0,
      "codec_name": "h264",
      "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
      "profile": "High",
      "codec_type": "video",
      "codec_tag_string": "avc1",
      "codec_tag": "0x31637661",
      "width": 1280,
      "height": 1440,
      "coded_width": 1280,
      "coded_height": 1440,
      "closed_captions": 0,
      "film_grain": 0,
      "has_b_frames": 2,
      "sample_aspect_ratio": "1:1",
      "display_aspect_ratio": "8:9",
      "pix_fmt": "yuv420p",
      "level": 40,
      "chroma_location": "left",
      "field_order": "progressive",
      "refs": 1,
      "is_avc": "true",
      "nal_length_size": "4",
      "id": "0x1",
      "r_frame_rate": "30/1",
      "avg_frame_rate": "30/1",
      "time_base": "1/15360",
      "start_pts": 0,
      "start_time": "0.000000",
      "duration_ts": 6023680,
      "duration": "392.166667",
      "bit_rate": "1772918",
      "bits_per_raw_sample": "8",
      "nb_frames": "11765",
      "extradata_size": 47,
      "disposition": {
        "default": 1,
        "dub": 0,
        "original": 0,
        "comment": 0,
        "lyrics": 0,
        "karaoke": 0,
        "forced": 0,
        "hearing_impaired": 0,
        "visual_impaired": 0,
        "clean_effects": 0,
        "attached_pic": 0,
        "timed_thumbnails": 0,
        "non_diegetic": 0,
        "captions": 0,
        "descriptions": 0,
        "metadata": 0,
        "dependent": 0,
        "still_image": 0
      },
      "tags": {
        "language": "und",
        "handler_name": "VideoHandler",
        "vendor_id": "[0][0][0][0]",
        "encoder": "Lavc60.31.102 libx264"
      }
    }
  ],
  "format": {
    "filename": "scene01.mp4",
    "nb_streams": 1,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "392.166667",
    "size": "87053127",
    "bit_rate": "1775839",
    "probe_score": 100,
    "tags": {
      "major_brand": "isom",
      "minor_version": "512",
      "compatible_brands": "isomiso2avc1mp41",
      "encoder": "Lavf60.16.100"
    }
  }
}
```

[^1]: OCEL is a standard designed to facilitate the exchange of object-centric event data across various case notions. 
The [OCEL website](www.ocel-standard.org) gives further information. 