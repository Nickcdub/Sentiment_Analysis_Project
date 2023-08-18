Project Evaluation for Sentiment Analysis


CONVENTIONAL NEURAL NETWORKS (CNN)
_________________________________________________________________
******************************************************************
******************************************************************
_________________________________________________________________


MODEL SUMMARY
_________________________________________________________________
_________________________________________________________________

Vocabulary size: 11219
Maximum length: 434
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 embedding (Embedding)       (None, 434, 100)          1121900   
                                                                 
 conv1d (Conv1D)             (None, 427, 32)           25632     
                                                                 
 max_pooling1d (MaxPooling1  (None, 213, 32)           0         
 D)                                                              
                                                                 
 flatten (Flatten)           (None, 6816)              0         
                                                                 
 dense (Dense)               (None, 10)                68170     
                                                                 
 dense_1 (Dense)             (None, 1)                 11        
                                                                 
=================================================================
Total params: 1215713 (4.64 MB)
Trainable params: 1215713 (4.64 MB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________





EPOCHS
_________________________________________________________________
_________________________________________________________________

Epoch 1/20
58/58 - 2s - loss: 0.5986 - accuracy: 0.6607 - 2s/epoch - 39ms/step
Epoch 2/20
58/58 - 2s - loss: 0.1286 - accuracy: 0.9545 - 2s/epoch - 34ms/step
Epoch 3/20
58/58 - 2s - loss: 0.0215 - accuracy: 0.9940 - 2s/epoch - 33ms/step
Epoch 4/20
58/58 - 2s - loss: 0.0037 - accuracy: 0.9995 - 2s/epoch - 33ms/step
Epoch 5/20
58/58 - 2s - loss: 0.0023 - accuracy: 0.9995 - 2s/epoch - 35ms/step
Epoch 6/20
58/58 - 2s - loss: 0.0015 - accuracy: 0.9995 - 2s/epoch - 32ms/step
Epoch 7/20
58/58 - 2s - loss: 0.0017 - accuracy: 0.9995 - 2s/epoch - 30ms/step
Epoch 8/20
58/58 - 2s - loss: 0.0012 - accuracy: 0.9995 - 2s/epoch - 27ms/step
Epoch 9/20
58/58 - 2s - loss: 0.0011 - accuracy: 0.9995 - 2s/epoch - 28ms/step
Epoch 10/20
58/58 - 2s - loss: 0.0018 - accuracy: 0.9989 - 2s/epoch - 30ms/step
Epoch 11/20
58/58 - 2s - loss: 0.0013 - accuracy: 0.9995 - 2s/epoch - 27ms/step
Epoch 12/20
58/58 - 2s - loss: 0.0011 - accuracy: 0.9995 - 2s/epoch - 28ms/step
Epoch 13/20
58/58 - 2s - loss: 0.0011 - accuracy: 0.9989 - 2s/epoch - 28ms/step
Epoch 14/20
58/58 - 2s - loss: 0.0010 - accuracy: 0.9995 - 2s/epoch - 28ms/step
Epoch 15/20
58/58 - 2s - loss: 9.7980e-04 - accuracy: 0.9995 - 2s/epoch - 28ms/step
Epoch 16/20
58/58 - 2s - loss: 0.0010 - accuracy: 0.9989 - 2s/epoch - 28ms/step
Epoch 17/20
58/58 - 2s - loss: 8.8730e-04 - accuracy: 0.9995 - 2s/epoch - 28ms/step
Epoch 18/20
58/58 - 2s - loss: 8.3099e-04 - accuracy: 0.9995 - 2s/epoch - 28ms/step
Epoch 19/20
58/58 - 2s - loss: 9.9527e-04 - accuracy: 0.9989 - 2s/epoch - 30ms/step
Epoch 20/20
58/58 - 2s - loss: 8.7033e-04 - accuracy: 0.9989 - 2s/epoch - 28ms/step
_________________________________________________________________


ACCURACY
_________________________________________________________________
Vocabulary size: 11219
Maximum length: 434
Train Accuracy: 99.95
Test Accuracy: 80.18


TEST RESULTS
_________________________________________________________________
_________________________________________________________________

Review: [Perhaps instead of hopping on bandwagon talking about against AI Art/VO, try to understand a little bit more nuance of AI generated material creation and don't just harass people who used it, especially for nonprofit.]
Sentiment: POSITIVE (54.498%)

Review: [My opinion on gatekeeping art changed when I saw so many people instantly turn to Gen AI falsely claiming that they were artists now too while celebrating the obsolescence of the very artists that fed the machine that made those garbage pictures. Justifying it as “innovation”.]
Sentiment: POSITIVE (82.924%)

Review: [AI ART IS INHERENTLY BAD. IT WILL ALWAYS BE BAD. THE VERY CORE OF WHAT IT DOES IS ART THEFT, THERE IS NO GETTING AROUND THAT. STOP USING IT. STOP PROMOTING IT. JUST STOP.]
Sentiment: POSITIVE (56.462%)

Review: [I love this shit, ai shouldn't replace art but i think it being another form is fine as long as people don't do the shit like acting like ai can or should replace actual art]
Sentiment: NEGATIVE (90.997%)

Review: [More and more I meet with the opinion that AI art is one evil thing, what cannon be trusted and be punished in all way... For me, it's a good way to look at characters from a slightly different angle and the motivation to make them better.]
Sentiment: POSITIVE (68.869%)

Review: [AI software takes things that real people made, and fakes making something new by using what it took. It's plagiarism by algorithm. If a human traced someone else's art, would it be plagiarism? ]
Sentiment: POSITIVE (59.341%)

Review: [AI algorithms can generate art, music, and even poetry, blurring the lines between human creativity and machine-generated content.]
Sentiment: POSITIVE (57.045%)

Review: [If man's did 95% of hard work and used AI once for something so small, it doesn't devalue his work, especially if it's for Portfolio. ]
Sentiment: POSITIVE (66.081%)

Review: [I don't think ai art should be banned. It should absolutely be a social enforcement. You cannot say ai art is bad and simultaneously defend lucky for doing it multiple times now. ]
Sentiment: NEGATIVE (83.477%)

Review: [Well, AI art isn't unethical in the first place. That said, unless you have produced a massive amount of art, you will probably not be able to produce a functioning model purely from your own art.]
Sentiment: NEGATIVE (66.470%)

Review: [AI Artificial Intelligence is getting dangerous too much Fake Fake Fake everywhere isn't good.]
Sentiment: NEGATIVE (70.697%)

Review: [Hope everyone is having a great day!! I’d kill to be relaxing on a yacht RN. Here’s some ai art I built of some dope yachts on the water. ]
Sentiment: POSITIVE (89.192%)

Review: [AI Art feels like an imitation, lacking the depth and raw emotion that real artists breathe into their creations. Let's not trade authenticity for shortcuts. ]
Sentiment: POSITIVE (58.230%)

Review: [AI-generated art might create visuals, but it lacks the heart and soul that human artists pour into their work. Our art tells stories; algorithms can't do that.]
Sentiment: POSITIVE (78.408%)

Review: [AI Art feels like a shallow mimicry of real artistry. It might paint pictures, but it'll never capture the feelings, experiences, and individuality of human creators.]
Sentiment: POSITIVE (87.661%)

Review: [Opening up about my AI art journey. As a content creator, it's not about cutting corners; it's about making the most of my resources and staying creative. ]
Sentiment: NEGATIVE (64.492%)

Review: [Unpacking the 'AI art guilt.' For me, it's a resourceful way to experiment with ideas, learn new styles, and make every pixel count. It's about being smart in creativity. ]
Sentiment: POSITIVE (56.288%)

Review: [Thoughts on AI art from a non-artist's perspective: It's less about art and more about self-expression. For those of us lacking talent, AI art lets me express my creativity without years of practice. ]
Sentiment: POSITIVE (94.307%)

Review: [So I decided to check out these AI art generators and I tried 3 of them and from what I’ve seen they are a scam.First, 90% of all features are behind a paywall.Second,You need to upload an image, so you need to have an art piece for the AI to make art. Third, quality is bad]
Sentiment: POSITIVE (81.308%)

Review: [Creativity is overrated and execution is underrated, something which effectively makes the execution magically accessible is disruptive to livelihoods, AI art is not inherently bad but is primarily going to be used to cut labor costs, which will most impact corporate contractors]
Sentiment: POSITIVE (56.722%)

Review: [People hear AI and instantly discredit anything having to do with it. That animation is so cool tho! The use of AI shouldnt make anyone ever look past the work put in. AI should be used as a tool instead of a medium. ]
Sentiment: POSITIVE (53.507%)

Review: [The creator still made something original and you can clearly see the craft which is the main argument against ai. AI can be a tool to assist and not just to replace. ]
Sentiment: NEGATIVE (75.519%)

Review: [Since reality is stressing me out so much lately I've been spending more time in solitude to rest my mind. AI art helps calm my ever-raw nerves these days.  I'm going to throw some of what I've done out there for giggles. ]
Sentiment: POSITIVE (51.190%)

Review: [I’ve gotta say that I watched the first episode and this might be one of the best things Marvel’s done since Endgame. I’m also feeling the fatigue and that a lot of it feels cash-grabby, but this one can stay so far, despite the AI.]
Sentiment: POSITIVE (98.140%)

Review: [So he used AI because it got him closer to what he imagined in his head and what he wanted - so that's exactly the danger of it. Art is never perfect, creators need to change, VA need to change and get new opportunities. AI is just bad for art in 99% of cases]
Sentiment: NEGATIVE (54.085%)