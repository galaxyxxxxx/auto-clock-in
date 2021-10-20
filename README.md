## Introduction

A auto clock-in script based on python3 for BJUTer.

It could clock in at 9:00 a.m everyday.

> The script is inspired by [tsosunchia](https://github.com/tsosunchia/bjut_autosignin)

## What can I do ?

- [x] Clock in at 9:00 a.m everyday
- [x] Send the email after clocking in

## Usage

1. Fork the project 

2. Settings
    Open the settings in your forking repository, add the following info to your secrets.

    ```
    EMAIL_USERNAME 
    EMAIL_FROM # usually equal to EMAIL_USERNAME
    EMAIL_TO # usually equal to EMAIL_USERNAME
    EMAIL_PASSWORD 
    EMAIL_SERVER
    EMAIL_PORT
    DATA
    ```

## Test
Run the script
```shell
python3 app.py
```

## Example

  Inspired by [tsosunchia](https://github.com/tsosunchia/bjut_autosignin)，I extract the user info module as a single file, which is easy for us to update own info.

  A example of `DATA` is listed as below. Also in DATA.json.template.

  ```json
  {
      "id": "402880c97b5d8ad1017c39dcd10*****",
      "token": "CA6CD39AFDAC284ED68BB81BD54*****",
      "JSESSIONID": "02F83B0ECCC5B8A051564CCC********-n1.jvm1",
      "c1": "在籍本科生",
      "c2": "在校内居住",
      "c3": "否",
      "c4": "否",
      "c5": "正常",
      "c6": "正常",
      "c7": "无情况",
      "c8": "在京内",
      "c12": "北京市,北京市,朝阳区,",
      "c9": "否",
      "c10": "否",
      "c11": "否",
      "c14": "未接种",
      "location_longitude": "40",
      "location_latitude": "110",
      "location_address": "北京市朝阳区平乐园100号北京工业大学"
  }
  ```

  ## Thanks
  ✨ [Woodykaixa](https://github.com/Woodykaixa)
  ✨ [galaxyxxxxx](https://github.com/galaxyxxxxx)
