My system is called “Composition 8008.” To create a drawing, simply run the file KandinskyMarkov.py and enter how many shapes you want in your piece. The system will create a drawing incorporating shapes found in Vasily Kandinsky's Composition 8. This program incorporates three shapes from Kandinsky's work: concentric yellow and blue circles, yellow triangles, and concentric pink and purple circles. The system incorporates Markov chains in choose which shapes follow each other. When a shape is drawn, the next shape is picked based on a transitional matrix of probabilities. 


When I was first reading about Markov chains, my mind instantly went to abstract art. There is no right or wrong in what a computer could design with regards to abstract art, so I wanted to program a system that would create its own artwork. I really like the painting “Composition 8" by Kandinsky so I chose three elements of the painting that stood out to me and recreated them with turtles. I like how my system is able to not only create its own “painting” but that the painting is completely different every time it is run. Though my piece is modeled specifically on Composition 8, I looked at other Kandinsky paintings that incorporate these shapes and colors to determine a general idea of probabilities for the transition matrix. 


I haven’t had experience with coding my own algorithms before, so it was a challenge to design both the general Markov framework and incorporate the artistic aspect at the same time. I also pushed myself to experiment more with the Turtles in Python. My only other experience with Turtles was completing the painting in Intro, so working with shapes that would generate and draw themselves was new to me. Since I am a TA for intro I wanted to be more comfortable with Turtles in case students need help with their work. 


I am interested in ways I could modify this code to incorporate more shapes or the styles of more artists. I had initially wanted to make a program that incorporated a lot more than just three shapes and also wanted to incorporate some of the designs in furniture and wallpaper that I found around campus. However, since the matrix for transitional probabilities increases exponentially each time an element is added, this turned out to be too complicated. I would be interested in using more shapes in my design going forward. I also hadn’t had experience using math or probability in Python, so figuring out how to use the weighted random choices based on my transitional matrix was a new challenge. 


My system is creative because it draws its own images, and the images are different each time the system is run. My system draws from familiar elements (Kandinsky’s shapes) but uses them in new ways. I think the pieces it produces are visually appealing as well. 


Sources I used: 

https://www.guggenheim.org/artwork/1924

https://www.datacamp.com/community/tutorials/markov-chains-python-tutorial

https://stackoverflow.com/questions/24636271/python-turtle-draw-concentric-circles-using-circle-method

https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
