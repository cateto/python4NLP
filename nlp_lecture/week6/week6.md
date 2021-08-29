#### NLP = NLU + NLG

NLG(Natural Language Generation)가 필요한 분야 ( ex : image captinoing, chatbot, machine translation )



#### Machine Translation 

Rule based(1980) -> Statistical (2015) -> Neural ==> 성능의 향상!!!



#### How~?

1. 워드임베딩 => 연속적인 표현에 강함!
2. SMT(통계번역) 는 여러 모듈이 결합-> End to End 모델은 하나의 모듈이 작동하는 방식

3. Attention으로 인해 길이가 긴 문장이 좋은 성능을 보이기 시작!



#### RNN

현재시점의 출력이 다음 시점의 입력으로 사용!

매 step마다 다중 클래스 분류

**Teacher Forcing 훈련기법** 

: 안쓰면 ? 중간에 한번이라도 잘못 예측하면 뒤의 결과가 뒤틀림. 그리고 학습 시간이 오래걸림.

: 쓰면 ?  훈련할떄는 실제 값=정답(label)으로 훈련하여 빠르게 훈련!

**Brnn으로 rnn lm을 구현할 수 있을까?** 

: Nope! 구현할 수 없다

q1. 기존에 brnn은 그럼 어떨때 쓰는지?

기존의 텍스트 분류나 many to many(개체명 인식 같은)문제에는 괜찮음.



#### Seq2Seq

입력된 시퀀스에서 다른 도메인의 시퀀스 출력.

문장을 넣었을때 문장이 나오는 모델.

인코더와 디코더 구조를 가지고 있다.

rnn이 있다고 생각~

인코더 (NLU) / 디코더 (NLG)



cf. RNN으로 번역기 제안 (인코더와 디코더 구조 제시, 통계번역기에 적용함)

cf2. Seq to Seq Learning with~~ 논문

: 서로 다른 두개의 LSTM 아키텍처를 각각 인코더 - 디코더로 사용.

디코더 (RNN의 다음 문장 예측)



q2. 번역기 학습하려면 어떤 데이터 셋이 있어야 하는가?

원어 - 번역결과 의 쌍의 데이터 셋이 있어야 함.

최소 200만개의 병렬문장이 있어야 하는데....구하기가 힘듦 ,, ㅎㅎ



q3. Teacher Forcing 은 어떤 원리로 적용되나요?

디코더부분을 개체명 인식하는 것처럼 many to many 라벨링 데이터와의 오차를 구해서 학습시킴

학습할때는 데이터셋이 3개 있어야 함. 

(원어 , EOS, 결과값)



q4. 그러면 인코더는 다대일 출력구조로 학습되고,
디코더만 다대다 teacher forcing을 사용하여 학습되는게 맞나요??

거의 다 맞는데 약간 애매한 것은 

인코더는 다대일 출력구조로 마지막 hidden state를 주고

디코더는 다대다 예측 구조!



인코더 rnn은 입력문장을 인코딩 한다. 그리고 마지막 hidden state를 결괏값으로

디코더 rnn에 전달한다. 

디코더 rnn은 랭귀지 모델이다. 번역될 문장을 생성하는!(이전 단어들로 다음단어 예측)

and

54p 슬라이드 : 학습단계에서는 teacher forcing을 쓰기땜에 테스트 단계랑 좀 다를거임 ㅋ



#### Beam Search

가설 : 매 스텝마다 확률 높은 k개의 정답 추적 eos를 만난 경우가 k개가 될때까지 반복



q5. k가 될때까지 반복?

조합하고자 하는 문장을 3개... 종료 토큰이 나오는게 3개 될때까지.



q6. 정답일 확률이 높다는거는 어떤식으로 계산하나요?

확률 곱!



q7. 확률 총합이 1이 되는건가?

아닙니다. 상위 3개만 가져오기떄문에 1보다는 낮음.



#### Subword Tokenization

- oov 문제 : 임베딩 matrix에 없는 단어면 unk 토큰으로 매칭
- oov를 없애기 위해 byte pair encoding 제안
- **byte pair encoding** : 모든 알파벳을 vocab에 추가 -> 자주 등장하는 pair는 새로운 byte가 된다.
- oov가 줄어드는 이유 : byte pair로 만들면 접사, 등등 분리되므로 새로보이는 단어에도 대처할 수 있다.
- byte pair tokenizer : vocab기준으로 토큰화 시킴! 



q8. lo, low.. ow는 추가안됨?

넵 추가 안됨. 전체 단어 집합에서 많이 등장하는 sub 워드로 구성됨, 

q9. byte pair tokenizer가 형태소 분석 보다 성능이 좋은가?

단어 5만개로 하면 sentencepiece가 더 성능 좋음, 단어 10만개 되니가 mecab이 더 성능 좋음..

토큰화속도는 메캅이 제일 빠름. 그런데 sentencepiece가 더 빠름.

성능 평가할때는 눈으로 볼 필요가 있음.

메캅은 신조어 같은 것 사전 추가해서 단어를 잘 토큰화할 수 있음.



요새는 mecab먼저 쓴 다음에 sentence piece를 사용할 수도 있다.

#### Huggingface라는 스타트업의 subword tokenizer



#### subword tokenizer은 원래 디토큰화를 위한 장치를 적용. '_' 를 붙이면 자연스럽게 다시 복원.

q10. mecab같은 경우에는 복원 어떻게 하는지?

mecab에다가 추가적으로 '_' 넣는 알고리즘을 넣어야 함.

q11. 토큰화할 때 단어 내에서 길이가 긴 조합으로 먼저 나누나요??

처음에 알파벳으로 다 쪼개고 -> 길이가 긴 조합이 나올때까지 합함.



소스 설명

masking layer : 패딩 고려 x 하도록 만듦.

q12. encoder_outputs, state_h, state_c = encoder_lstm(enc_masking) 여기서 enc_masking을 파라미터로 넣어주는 부분 이해가 안 되어 이 부분 설명해주실 수 있나요? 

패딩 토큰 연산에서 제외함.

q13. 제가 놓쳤을 수도 있는데 .. return_sequences=True 했을때 매 timestep마다 결괏값이 추출되는건가요? 그리고 결괏값은 어디에 저장되는 지 궁금합니다.

4주차 simple RNN LSTM실습하기 에서 확인해보면 됨!

decoder_outputs에 저장이 됨.



인코더는 모델 구조가 안바뀜

디코더는 상세하게 쪼개놓음.

학습 단계랑 다른점 : decoder의 모델에서 encoder의 hidden states를 초기 입력값으로 하는데 반해

decoder에서 이전 시점의 상태를 initial_state로 구성함.



https://ko.flitto.com/language/translation/text



과제 ) 











