# Rhasspy TTS Home Assistant Integration
TTS platform to enable home assistant to use the [rhasspy](https://rhasspy.readthedocs.io/en/latest/) text-to-speech engine.

## Installation

Install via HACS or copy `./custom_components/rhasspy_tts/` to `/config/custom_components/`

## Configuration Variables

|  key    | required | value             | description |
|---------|----------|-------------------|-------------|
|platform | yes      | `rhasspy_tts`     |             |
|host     | no       | `127.0.0.1`       | Hostname or IP address of the rhasspy server |
| port    | no       | `12101`            | Port to stream audio to, default is `12101` |
| ssl     | no       | `true`            | Enable this if rhasspy is running with ssl enabled |

## Example Config

```yaml
tts:
  - platform: rhasspy_tts
```
