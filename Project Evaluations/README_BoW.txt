Project Evaluation for Sentiment Analysis


BAG-OF-WORDS
_________________________________________________________________
******************************************************************
******************************************************************
_________________________________________________________________


MODEL SUMMARY
_________________________________________________________________
_________________________________________________________________



Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 dense (Dense)               (None, 50)                729050    
                                                                 
 dense_1 (Dense)             (None, 1)                 51        
                                                                 
=================================================================
Total params: 729101 (2.78 MB)
Trainable params: 729101 (2.78 MB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________



EPOCHS
_________________________________________________________________
_________________________________________________________________




Epoch 1/20
101/101 - 0s - loss: 0.6620 - accuracy: 0.5941 - 327ms/epoch - 3ms/step
Epoch 2/20
101/101 - 0s - loss: 0.5480 - accuracy: 0.8675 - 188ms/epoch - 2ms/step
Epoch 3/20
101/101 - 0s - loss: 0.3979 - accuracy: 0.9512 - 166ms/epoch - 2ms/step
Epoch 4/20
101/101 - 0s - loss: 0.2783 - accuracy: 0.9642 - 170ms/epoch - 2ms/step
Epoch 5/20
101/101 - 0s - loss: 0.1986 - accuracy: 0.9801 - 167ms/epoch - 2ms/step
Epoch 6/20
101/101 - 0s - loss: 0.1474 - accuracy: 0.9872 - 173ms/epoch - 2ms/step
Epoch 7/20
101/101 - 0s - loss: 0.1128 - accuracy: 0.9907 - 166ms/epoch - 2ms/step
Epoch 8/20
101/101 - 0s - loss: 0.0880 - accuracy: 0.9947 - 177ms/epoch - 2ms/step
Epoch 9/20
101/101 - 0s - loss: 0.0698 - accuracy: 0.9953 - 171ms/epoch - 2ms/step
Epoch 10/20
101/101 - 0s - loss: 0.0562 - accuracy: 0.9963 - 168ms/epoch - 2ms/step
Epoch 11/20
101/101 - 0s - loss: 0.0459 - accuracy: 0.9975 - 178ms/epoch - 2ms/step
Epoch 12/20
101/101 - 0s - loss: 0.0379 - accuracy: 0.9981 - 176ms/epoch - 2ms/step
Epoch 13/20
101/101 - 0s - loss: 0.0317 - accuracy: 0.9984 - 178ms/epoch - 2ms/step
Epoch 14/20
101/101 - 0s - loss: 0.0267 - accuracy: 0.9991 - 173ms/epoch - 2ms/step
Epoch 15/20
101/101 - 0s - loss: 0.0226 - accuracy: 0.9994 - 168ms/epoch - 2ms/step
Epoch 16/20
101/101 - 0s - loss: 0.0193 - accuracy: 0.9994 - 169ms/epoch - 2ms/step
Epoch 17/20
101/101 - 0s - loss: 0.0166 - accuracy: 0.9997 - 165ms/epoch - 2ms/step
Epoch 18/20
101/101 - 0s - loss: 0.0145 - accuracy: 0.9997 - 179ms/epoch - 2ms/step
Epoch 19/20
101/101 - 0s - loss: 0.0127 - accuracy: 0.9997 - 173ms/epoch - 2ms/step
Epoch 20/20
101/101 - 0s - loss: 0.0112 - accuracy: 0.9997 - 171ms/epoch - 2ms/step
Test Accuracy: 88.604653
_________________________________________________________________


SUMMARY STATISTICS
_________________________________________________________________
_________________________________________________________________

          binary      count      tfidf       freq
count  10.000000  10.000000  10.000000  10.000000
mean    0.839302   0.861163   0.840698   0.881395
std     0.006972   0.009991   0.016196   0.000000
min     0.830233   0.839535   0.804651   0.881395
25%     0.834884   0.856977   0.836047   0.881395
50%     0.837209   0.863954   0.841860   0.881395
75%     0.845349   0.868605   0.850000   0.881395
max     0.851163   0.872093   0.862791   0.881395


ACCURACY
_________________________________________________________________
Test Accuracy: 88.604653
Training Accuracy: 99.97


TEST RESULTS
_________________________________________________________________
_________________________________________________________________

Review: [Perhaps instead of hopping on bandwagon talking about against AI Art/VO, try to understand a little bit more nuance of AI generated material creation and don't just harass people who used it, especially for nonprofit.]
Sentiment: NEGATIVE (76.993%)

Review: [My opinion on gatekeeping art changed when I saw so many people instantly turn to Gen AI falsely claiming that they were artists now too while celebrating the obsolescence of the very artists that fed the machine that made those garbage pictures. Justifying it as “innovation”.]
Sentiment: POSITIVE (60.996%)

Review: [AI ART IS INHERENTLY BAD. IT WILL ALWAYS BE BAD. THE VERY CORE OF WHAT IT DOES IS ART THEFT, THERE IS NO GETTING AROUND THAT. STOP USING IT. STOP PROMOTING IT. JUST STOP.]
Sentiment: POSITIVE (62.291%)

Review: [I love this shit, ai shouldn't replace art but i think it being another form is fine as long as people don't do the shit like acting like ai can or should replace actual art]
Sentiment: NEGATIVE (89.781%)

Review: [More and more I meet with the opinion that AI art is one evil thing, what cannon be trusted and be punished in all way... For me, it's a good way to look at characters from a slightly different angle and the motivation to make them better.]
Sentiment: POSITIVE (82.727%)

Review: [AI software takes things that real people made, and fakes making something new by using what it took. It's plagiarism by algorithm. If a human traced someone else's art, would it be plagiarism? ]
Sentiment: NEGATIVE (68.482%)

Review: [AI algorithms can generate art, music, and even poetry, blurring the lines between human creativity and machine-generated content.]
Sentiment: NEGATIVE (51.797%)

Review: [If man's did 95% of hard work and used AI once for something so small, it doesn't devalue his work, especially if it's for Portfolio. ]
Sentiment: NEGATIVE (64.995%)

Review: [I don't think ai art should be banned. It should absolutely be a social enforcement. You cannot say ai art is bad and simultaneously defend lucky for doing it multiple times now. ]
Sentiment: NEGATIVE (89.342%)

Review: [Well, AI art isn't unethical in the first place. That said, unless you have produced a massive amount of art, you will probably not be able to produce a functioning model purely from your own art.]
Sentiment: NEGATIVE (92.245%)

Review: [AI Artificial Intelligence is getting dangerous too much Fake Fake Fake everywhere isn't good.]
Sentiment: POSITIVE (72.866%)

Review: [Hope everyone is having a great day!! I’d kill to be relaxing on a yacht RN. Here’s some ai art I built of some dope yachts on the water. ]
Sentiment: POSITIVE (94.384%)

Review: [AI Art feels like an imitation, lacking the depth and raw emotion that real artists breathe into their creations. Let's not trade authenticity for shortcuts. ]
Sentiment: POSITIVE (72.078%)

Review: [AI-generated art might create visuals, but it lacks the heart and soul that human artists pour into their work. Our art tells stories; algorithms can't do that.]
Sentiment: POSITIVE (69.011%)

Review: [AI Art feels like a shallow mimicry of real artistry. It might paint pictures, but it'll never capture the feelings, experiences, and individuality of human creators.]
Sentiment: POSITIVE (79.628%)

Review: [Opening up about my AI art journey. As a content creator, it's not about cutting corners; it's about making the most of my resources and staying creative. ]
Sentiment: NEGATIVE (69.731%)

Review: [Unpacking the 'AI art guilt.' For me, it's a resourceful way to experiment with ideas, learn new styles, and make every pixel count. It's about being smart in creativity. ]
Sentiment: POSITIVE (74.078%)

Review: [Thoughts on AI art from a non-artist's perspective: It's less about art and more about self-expression. For those of us lacking talent, AI art lets me express my creativity without years of practice. ]
Sentiment: POSITIVE (90.131%)

Review: [So I decided to check out these AI art generators and I tried 3 of them and from what I’ve seen they are a scam.First, 90% of all features are behind a paywall.Second,You need to upload an image, so you need to have an art piece for the AI to make art. Third, quality is bad]
Sentiment: NEGATIVE (69.924%)

Review: [Creativity is overrated and execution is underrated, something which effectively makes the execution magically accessible is disruptive to livelihoods, AI art is not inherently bad but is primarily going to be used to cut labor costs, which will most impact corporate contractors]
Sentiment: POSITIVE (56.352%)

Review: [People hear AI and instantly discredit anything having to do with it. That animation is so cool tho! The use of AI shouldnt make anyone ever look past the work put in. AI should be used as a tool instead of a medium. ]
Sentiment: NEGATIVE (60.916%)

Review: [The creator still made something original and you can clearly see the craft which is the main argument against ai. AI can be a tool to assist and not just to replace. ]
Sentiment: NEGATIVE (83.806%)

Review: [Since reality is stressing me out so much lately I've been spending more time in solitude to rest my mind. AI art helps calm my ever-raw nerves these days.  I'm going to throw some of what I've done out there for giggles. ]
Sentiment: NEGATIVE (71.406%)

Review: [I’ve gotta say that I watched the first episode and this might be one of the best things Marvel’s done since Endgame. I’m also feeling the fatigue and that a lot of it feels cash-grabby, but this one can stay so far, despite the AI.]
Sentiment: POSITIVE (98.910%)

Review: [So he used AI because it got him closer to what he imagined in his head and what he wanted - so that's exactly the danger of it. Art is never perfect, creators need to change, VA need to change and get new opportunities. AI is just bad for art in 99% of cases]
Sentiment: NEGATIVE (50.329%)


