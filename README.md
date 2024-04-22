# 상공회의소 인천인력개발원 인텔교육 1기

## Clone code 

```shell
git clone --recurse-submodules https://github.com/KCCIIC2/intel-01.git
```

* `--recurse-submodules` option 없이 clone 한 경우, 아래를 통해 submodule update

```shell
git submodule update --init --recursive
```

## Preparation

### Git LFS(Large File System)

* 크기가 큰 바이너리 파일들은 LFS로 관리됩니다.

* git-lfs 설치 전

```shell
# Note bin size is 132 bytes before LFS pull

$ find ./ -iname *.bin|xargs ls -l
-rw-rw-r-- 1 <ID> <GROUP> 132 Nov  6 09:41 ./mosaic-9.bin
-rw-rw-r-- 1 <ID> <GROUP> 132 Nov  6 09:41 ./mosaic-9.bin
-rw-rw-r-- 1 <ID> <GROUP> 132 Nov  6 09:41 ./ssdlite_mobilenet_v2_fp16.bin
-rwxrwxr-x 1 <ID> <GROUP> 132 Nov  6 09:41 ./ssdlite_mobilenet_v2_fp16.bin
```

* git-lfs 설치 후, 다음의 명령어로 전체를 가져 올 수 있습니다.

```shell
$ sudo apt install git-lfs

$ git lfs pull
$ find ./ -iname *.bin|xargs ls -l
-rw-rw-r-- 1 <ID> <GROUP> 3358630 Nov  6 09:41 ./mosaic-9.bin
-rw-rw-r-- 1 <ID> <GROUP> 3358630 Nov  6 09:41 ./mosaic-9.bin
-rw-rw-r-- 1 <ID> <GROUP> 8955146 Nov  6 09:41 ./ssdlite_mobilenet_v2_fp16.bin
-rwxrwxr-x 1 <ID> <GROUP> 8955146 Nov  6 09:41 ./ssdlite_mobilenet_v2_fp16.bin
```

### 환경설정

* [Ubuntu](./doc/environment/ubuntu.md)
* [OpenVINO](./doc/environment/openvino.md)
* [OTX](./doc/environment/otx.md)

## Team projects

### 제출방법

1. 팀구성 및 프로젝트 세부 논의 후, 각 팀은 프로젝트 진행을 위한 Github repository 생성

2. [doc/project/README.md](./doc/project/README.md)을 각 팀이 생성한 repository의 main README.md로 복사 후 팀 프로젝트에 맞게 수정 활용

3. 과제 제출시 `인텔교육 1기 Github repository`에 `New Issue` 생성. 생성된 Issue에 하기 내용 포함되어야 함.

    * Team name : Project Name
    * Project 소개
    * 팀원 및 팀원 역활
    * Project Github repository
    * Project 발표자료 업로드

4. 강사가 생성한 `Milestone`에 생성된 Issue에 추가 

### 평가방법

* [assessment-criteria.pdf](./doc/project/assessment-criteria.pdf) 참고

### 제출현황

### Team: EcoSort - 소리인식 기반 재활용 시스템
<프로젝트 요약><br>
EcoSort는 혁신적인 음성인식 기술을 활용하여 효율적인 자동 쓰레기 분류 시스템을 개발하는 프로젝트입니다. 이 시스템은 쓰레기를 던져서 쓰레기통 윗부분에 부딪혀 만드는 소리를 인식하여 해당 쓰레기가 플라스틱, 철, 종이 중 어느 것인지 식별하고 분류하는 기능을 제공합니다.

이 프로젝트는 환경 보호를 위한 혁신적인 기술의 결합을 통해 쓰레기 처리의 효율성과 편의성을 증대시킵니다. 쓰레기 분류는 많은 사람들이 소홀히 하는 문제 중 하나입니다. 따라서 EcoSort는 이러한 문제를 해결하고자 음성인식 기술을 활용하여 쓰레기를 자동으로 분류함으로써 환경 보호 의식을 높이고 쓰레기 처리 과정을 최적화하는 것을 목표로 합니다.

* Members
  | Name | Role |
  |----|----|
  | 김승환 | Project lead, 프로젝트를 총괄하고 마일스톤을 생성하고 프로젝트 이슈 진행상황을 관리한다. |
  | 송인태 | Embedded system , 기구및 제어 시스템을 제작하고, 펌웨어를 코딩한다. |
  | 김용철 | AI modeling, 재활용 소재에 대한 음성 인식 AI를 모델링 한다. |
  | 김준영 | Assistant, 전반적인 도움 및 문서작업 보조 |
* [프로젝트 깃허브 주소](https://github.com/CodeMystero/soundRecognitionRecycleBin)
* [발표자료](https://www.canva.com/design/DAGB4bD7V8c/_7ljApcovK_1GcbWy087zg/edit?utm_content=DAGB4bD7V8c&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

