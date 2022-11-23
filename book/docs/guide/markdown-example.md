# Writing Rules (Markdown)

```{admonition} 추천 작성 환경
- Visual Studio Code
  - MyST markdown extention
  - Markdown extention
  - Jupyter-notebook extention
```


### 1. 본문 작성
(1) 제목 
- 제목은 최상단에 Header-lv1으로 간결하게 기입한다. 
- 논문 리뷰의 경우 제목은 리뷰하고자 하는 논문의 nickname또는 논문 제목과 투고된 학회/학술지 명을 다음과 같은 양식으로 기재한다. 

  ```plaintext
  {"NickName or 제목"} - {"학회/학술지 명"}
  ```

(2) 논문 정보를 기재한다. 
- Jupyter-book의 "admonition" block에 다음과 같은 양식으로 기입한다. 
- review 항목은 openReview 등 정식 리뷰 결과에 한정하여 기입한다.

  ````plaintext
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
  ````

```{admonition} Information
- **Title:** Instance-sensitive Fully Convolutional Networks, ECCV 2016

- **Reference**
    - Paper: [https://arxiv.org/abs/1603.08678](https://arxiv.org/abs/1603.08678)

- **Review By:** 

- **Last updated on Nov. 1, 2022**
```


(2). 본문에 image를 추가하는 경우 다음 format을 이용한다. 
- 영상 파일 경로는 작성하는 markdown 문서의 상대경로로 입력한다.
- figure-tag는 본문의 referencing을 위해 다른 그림과 구분될 수 있는 값으로 지정한다.    
- 아카이브 cite No.를 기준으로 출처를 기입한다. e.g. arXiv:1803.10464

  ````plaintext
  :::{figure-md} 'tag명'
  <img src="{주소}" alt="{tag명}" class="bg-primary mb-1" width="{영상 크기}">

  {제목} \  (source: {출처})
  :::
  ````


:::{figure-md} lenna
<img src="pic/Lenna.png" 
alt="lenna" 
class="bg-primary mb-1" 
width="300px">

Lenna (width=300px) \  (source: [wiki]("https://en.wikipedia.org/wiki/Lenna#/media/File:Lenna_(test_image).png"))
:::

- 본문 내 figure를 인용하는 경우 다음과 같이 reference 형식을 사용한다. (e.g. {numref}`lenna`)
  
  ````plaintext
  {ref}`{figure-tag}`
  # e.g. 
  {numref}`lenna`
  ````
  - [https://jupyterbook.org/en/stable/content/figures.html#referencing-figures](https://jupyterbook.org/en/stable/content/figures.html#referencing-figures)

- image의 index가 추가될 필요가 없는 경우 (논문 내 table 등) 추가하는 경우 다음 양식을 활용한다. 
- 
  ````plaintext
  ```{image} pic/Lenna.png
  :alt: aff9.png
  :class: bg-primary mb-1
  :align: center
  :width: 300
  ```
  ````

    ```{image} pic/Lenna.png
  :alt: lenna2.png
  :class: bg-primary mb-1
  :align: center
  :width: 300
  ```


  


## Reference

- jupyter-book syntax: (https://jupyterbook.org/reference/cheatsheet.html#myst-syntax-cheat-sheet)