# JupyterBook 기본 사용법

## install dependencies

- Jupyter book 및 GitHub Pages Import package 설치

    ```bash
    pip install -U jupyter-book
    pip install ghp-import
    ```

## jupyter book build

- init
  - 페이지 작성은 `.md`, `.ipynb` 형식으로 작성

- git clone 

  - ```bash
    cd "{work directory}"
    git clone https://github.com/Pseudo-Lab/Review-archives.git
    ```

- 페이지 작성 파일 이동

  - `SegCrew-Book/book/docs` 에 위치시킬 것
  -  폴더 내에 작성

- `_toc.yml` 변경

  - `Review-archives/book` 내 `_toc.yml` 파일 변경

  - ```yaml
	format: jb-book
	root: docs/index
	chapters:
	- file: docs/study01/PageLv1
	  sections:
	  - file: docs/study01/PageLv2-1
      	  sections:
    	  - file: docs/study01/PageLv2-1-1
          - file: docs/study01/PageLv2-1-2
	  - file: docs/study01/PageLv2-2
	  - file: docs/study01/PageLv2-3
	- file: docs/study02/PageLv1
	  sections:
	  - file: docs//study02/PageLv2-1
      - file: docs//study02/PageLv2-2
    ```

  - 위 코드 참조하여 추가한 페이지 이름 변경


- Jupyter book build

  - ```bash
    cd "{work directory}"/Review-archives
    jupyter-book build book/
    ```

  -`"{work directory}"/build/html/index.html`을 통해 build 결과물을 확인할 수 있다.

- Publish

  - git repo에 변경 내용을 push 한다. (PR로 변경 예정)

  - ```bash
    git add .
    git commit -m "MOD ~~~"
    git push
    ```

  - GitHub Page publisher를 이용하여 빌드된 jupyter-book을 publish한다.
    ```bash
    pip install ghp-import
    ghp-import -n -p -f book/_build/html -m "20-08-09 publishing"
    ```

  - https://pseudo-lab.github.io/Review-archives/ 링크 접속

## Writing Rules

[jupyter-book syntax]

https://jupyterbook.org/reference/cheatsheet.html#myst-syntax-cheat-sheet

1. 제목은 리뷰하고자 하는 논문의 nickname또는 논문 제목과 투고된 학회/학술지 명을 다음과 같은 양식으로 기재한다. 

```plaintext
{"NickName or 제목"} - {"학회/학술지 명"}
```

2. 본문 최상단에 논문 정보를 기재한다. 
- Jupyter-book의 "admonition" block에 다음과 같은 양식으로 기입한다. 
- review 항목은 openReview 등 정식 리뷰 결과에 한정하여 기입한다.

```plaintext
```{admonition} Information
- **Title:** {논문 제목}, {학회/학술지명}

- **Reference**
    - Paper:  [{논문 링크}]({논문 링크})
    - Code: [{code 링크}]({code 링크})
    - Review: [{review 링크}]({review 링크})
    
- **Review By:** {리뷰 작성자 기입}

- **Edited by:** {리뷰 편집자 기입}

- **Last updated on {최종 update 날짜 e.g. Jan. 5, 2022}**
```
```
3. 본문에 image를 추가하는 경우 다음 format을 이용한다. 
- figure-tag는 본문의 referencing을 위해 다른 그림과 구분될 수 있는 값으로 지정한다.    
-  아카이브 cite No.를 기준으로 출처를 기입한다. e.g. arXiv:1803.10464

```plaintext
:::{figure-md} 'tag명'
<img src="{주소}" alt="{tag명}" class="bg-primary mb-1" width="{800px}">

{제목} \  (source: {출처})
:::
```

- 논문의 표를 image로 추가하는 경우 다음 양식을 활용한다. 
```plaintext
 ```{image} pic/affinitynet/aff9.png
:alt: aff9.png
:class: bg-primary mb-1
:align: center
:width: 800
```
```
