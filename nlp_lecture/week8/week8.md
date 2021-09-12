#### Review

포지셔널인코딩 : 순서정보 RNN은 있지만, Transformer는 병렬로 입력받으므로 순서정보가 필요.

self-attention : Query = Key = Value (문장 하나에서 뽑아냄)

트랜스 포머의 2번째 층은 self-attention이 아님.



### 인코더!

#### Transformer

Transformer의 Add & Norm : 성능향상을 위한 부가적인 효과

Self-attention으로 문맥, 문장 내에서 다른 단어와의 관계 파악에 효과적



q1. 단어벡터의 차원이 512

모델이 크면 벡터 차원이 커지는게 맞음.



q2. 쿼리가중치, 키가중치, 밸류가중치도 역전파에 의해 조정되는 과정을 거치는건가요?

옙,, 그 과정은 한번 공부해보자 ㅠ



멀티헤드 = 하나하나를 다 concatenate한 것!!



#### Position-Wise FFNN

수식 보면 됨!



#### Add & Norm 

서브층을 지나면 무조건함. 

- Add = H(x) = x + F(x)
- 왜 해주는 건가? 이미지 처리 쪽에서 많이 사용되는데, 원래 입력이 손실될수 밖에 없으므로 손실되는 정보를 다시 더해서 보존해주는 효과가 있다.
- Norm : 텐서의 마지막 차원에 대해 평균과 분산을 구함.
- 원래 벡터르,ㄹ 수식에 넣어서 얻은 값을 덮어씌움!
- 

### 디코더!

#### masked multi head self attention

masking 해줌 => why? => [교사강요] 학습 시에는 실제 예측할 문장을 입력으로 넣어준다.

=>다음 단어 예측 모델이기때문에 => <sos>는 뒤 단어 못보게 하고 , 그 다음 단어는 그 뒤의 단어 못보게 하고...



q3. 디코더에서 다음 시점들의 단어 masking하는 건 모델 훈련과정에서만 이루어지는건가요?

테스트 과정에서는 실제로 다음 단어를 예측해야하기때문에 masking할것도 없음.



q4. traing 과정이니까 미리 답을 알면 좋은거 아닐까요..? 오버피팅 때문일까요?

학습과정에서도 문제를 잘 맞춰야 답 모르고 해도 맞출수잇어야함. 정답 보게 하면 오버피팅 발생



q5. Attention score 까지구하고 softmax 넣기 전에 마스킹해주는건가요~??

넵 (뒷부분에 설명)



q6. 자연어처리 task랑은 관련없는거죠~?

디코더 자체의 특성 때문에 masking하는것임. (transformer활용한 기계번역에서)



q7. test 데이터에서는 decoder의 입력에 어떤 문장이 들어가는 건가요??

테스트에는 <sos> <pad> <pad> <pad> 이런식으로 입력이 들어감.



q8. 그러면 매 예측단어마다 디코더 6층 모두 반복하는 건가요??

yes.



q9. position-wise ffnn은 하는 이유가 있나요?

신경망을 추가, 모델의 학습 여지를 늘려줌.



q10. 혹시 Transformer에서는
임베딩레이어도 학습하나요? 아니면 프리트레인 임베딩벡터를 사용하나요~??

굳이 안씀. 안쓰는게 좋음. 2-300만개를 학습하기때문에 의미가 없음. 이거 자체를 학습하는게 나음.

<카네기 멜론대학교 강의자료 : pretrained embedding을 안쓰는것을 추천하는 task>

-번역기

-언어모델 (다음 단어 예측)



### ELMo

언어모델로 부터 얻는 임베딩

순방향 ,역방향 학습 시켜서 임베딩 벡터로 하게되면 다의어 같은 것,, 문맥에 따른 단어 고려 가능.



ex) LSTM에 위키피디아 , E-book등으로 다음 단어 예측하도록 방대한 데이터로 학습

랜덤초기화된 LSTM



 Generative Pretraining Model

언어모델은 방향이 다음 단어를 예측하기때문에 단방향일수밖에없음,



so, Masked Language Model : K%의 단어를 [Mask]로 변경하여 이를 예측하도록 함.



### Bert

트랜스포머의 encoder를 12층 쌓아서 만듦



positional encoding 대신 position embedding 학습에 맡기기로!~~~~



q11. positional encoding은 단순 합이고 position embedding은 학습에 포함된다고하는데 조금 더 설명해주실수있나요?

positional encoding - 수학적으로 얻어내는 것

position embedding - positional encoding 대신 쓰긴 했는데



문장 길이 : 10

임베딩 벡터 차원 : 256



포지셔널 인코딩 (10x256) 행렬 만들고 (10x256) 문장 행렬에 더해준다.

포지셔널 임베딩 embedding(10, 256) 임베딩 층을 

0번 위치 단어 벡터 + 0번 포지셔널 임베딩 벡터

1번 위치 단어 벡터 + 1번 포지셔널 임베딩 벡터



#### [CLS] 토큰을 왜 붙이는가?

classification!!! 분류,,!!! 위치에 출력층(classifier) 붙이면 됨. 맨 앞



q12. 인코더를 어떻게 학습시키는지 조금 더 설명해주실 수 있나요?
Masked task랑 NSP task를 동시에 학습시키는지,
하나  task로 학습하고 또 다른 task로 학습시키는건지 모르겠어요ㅠㅠ
그리고 mask토큰은 모델 입력으로 쓸 때부터 있는건가요??



Masked 위에 출력층 붙여서 맞추도록 함.

오차를 구해서 역전파로 masked language model 훈련



NSP, masked 동시에 학습시키는 방법..?

오차의 양 다 더해서 하나의 오차를 만들어서 그 총 오차를 줄이는 방식으로 학습이 됨.



q13. 좀 벗어나는 질문일 수있는데 사전학습 이후에 fine tuning할때 다른 task를 동시에 사용할 수는 없나요? (예를 들면 개체명 인식 task + 텍스트 분류 task..)

할수는 있는데 그냥 따로하는게 더 나음 model 자체가 한방향으로 가는게 더 나음



q14. Bert에서 3가지 임베딩을 더한다는게 그냥 산술적인 덧셈이 맞죠? concatenate가 아니라

산술적 덧셈 맞음!



#### 타인이 만들어놓은 모델 쓸 때 필요한것

1) 모델 다운로드
2) 토크나이저 다운로드



<준비해야할 것>

token input

segment input은 문장 1개면 다 0, 문장 2개면 1,0

attention mask [pad]는 0 나머지는 1로 채운 attention mask



outputs[0] ; 모든 위치의 벡터(Many to Many)

outputs[1] ; cls위치의 벡터 (Many to One)



q15. SKT버전에서 버트가 트랜스포머 인코더여서 output[0]이 모든시점 벡터인게 이해가 안가는데, 
인코더에서 나오는 (문장길이, d_model) 행렬에서 
각 행을 한 시점의 벡터로 보는건가요~??

넵 맞습니다.

