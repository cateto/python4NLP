- 실시간 유사처리
  - 기존 : 수집한 데이터를 mysql full-text query를 통해 검색. 바이너리 비교를 통해 근실시간으로 부모 seq 매칭
  - ES : ~~~
  - FAISS : 
- FullText Search(전문검색)
  - 정의 : 게시물의 내용이나 제목 등과 같이 문장이나 문서의 내용에서 키워드를 검색하는 기능. 이름이나 별명 등과 같은 단어에서 일부만 일치하는 사용자를 검색하는 기능으로도 사용할 수 있다. LIKE 검색 (%%) 은 인덱스를 사용하지 못할 수도 있지만, FullText Search는 일부만 검색하는 경우에도 전문 검색 인덱스를 사용할 수 있으므로 더 빠른 검색이 가능하다.
  - 인덱싱 방식 : 본문에서 키워드를 분석하여 인덱스를 구축할 때 어떤 알고리즘을 사용할 것인가?
    - MySQL 5.1 ~ 5.6 버전 대에서는 N-gram 방식의 인덱싱을 지원하기 때문에 단어나 어휘를 고려하지 않고 본문의 내용을 모두 잘라서 인덱스를 만들어 사용하게 된다.
  - MySQL build-in FullText Search
    - MySQL 5.5 버전까지는 MyISAM Storage Engine을 사용하는 테이블에서만 사용할 수 있었다. 5.6 버전 부터는 InnoDB에서도 사용이 가능하도록 기능이 추가되었고, 5.7 부터는 중국어/한글/일본어를 대응할 수 있는 Parser의 N-gram이 설치되어 있고, Mecab도 플러그인으로 사용이 가능하다.
  - StopWords
    - MySQL의 기본 stopwords ```INFORMATION_SCHEMA.INNODB_FT_DEFAULT_STOPWORD```
    - ```stop word는 구분자라고도 표현하는데 대표적으로 띄워쓰기나 문장 기호 등을 기준으로 키워드를 추출해내고 그 결과를 인덱스로 구축하는 방식 입니다. 이러한 Stop word 방식은 키워드가 전부 일치하거나 prefix(전방) 가 일치할 때만 결과를 가져올 수 있습니다.```
    - ![image-20220111100010864](https://raw.githubusercontent.com/cateto/resources/main//img/image-20220111100010864.png)
  - 사용자 정의 Stopwords



- 벡터 검색의 적용 사례

  - 의미론적 텍스트 검색 (시맨틱 검색)

    - [시맨틱 검색](https://www.pinecone.io/docs/examples/semantic-text-search/)
    - [필터링이 포함된 하이브리드 검색](https://www.pinecone.io/docs/examples/basic-hybrid-search/)

  - 제품 추천

    - [Movie Recommender](https://www.pinecone.io/docs/examples/movie-recommender-system/)

  - FAQ 답변

  - 개인화

  - [이미지 유사성 검색](https://www.pinecone.io/docs/examples/image-similarity-search/)

  - 오디오 검색

  - 중복 제거

    - [문서 중복 제거](https://www.pinecone.io/docs/examples/document-deduplication/)

  - IT 이벤트 로그의 위협 감지

    - [IT 위협 탐지](https://www.pinecone.io/docs/examples/it-threat-detection/)

    

-  FAISS

  - FAISS에서 제공하는 기능

    - K-NN Clustering

    - ANN(Aproximate nearest neighbors)

      - [프로덕트 양자화기(Product Quantizer)](https://mccormickml.com/2017/10/13/product-quantizer-tutorial-part-1/)와 IndexIVFPQ 인덱스
      - vector index를 구축하여 검색 속도를 개선

    - K-means Clustering

      https://towardsdatascience.com/20x-times-faster-k-means-clustering-with-faiss-5e1681fa2654

    - 

  - 사례 위주 리서치

    - 당근 마켓 유사 게시물 처리(반복적인 게시글과 수익이 목적인 사용자를 방지)
      https://medium.com/daangn/%EB%8B%B9%EA%B7%BC%EB%A7%88%EC%BC%93%EC%97%90%EC%84%9C-%EB%94%A5%EB%9F%AC%EB%8B%9D-%ED%99%9C%EC%9A%A9%ED%95%98%EA%B8%B0-3b48844eba62

    - 당근 마켓 딥러닝 개인화 추천 시스템(첫 화면 추천 시스템)

      https://medium.com/daangn/%EB%94%A5%EB%9F%AC%EB%8B%9D-%EA%B0%9C%EC%9D%B8%ED%99%94-%EC%B6%94%EC%B2%9C-1eda682c2e8c

    - 핀터레스트 홈 피드 추천 시스템

      https://www.youtube.com/watch?v=hN995d7g4us

      - cadidate generation
        - 

    - 유투브 추천 시스템 논문

      https://research.google/pubs/pub45530/

  - 응용 위주 리서치

    - huggingface dataset에 faiss index 추가

      https://huggingface.co/docs/datasets/faiss_and_ea.html

