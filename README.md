# PongGame
A repository containing a minigame, Pong to be specific, that  i worked on to enhance my python skills
For start i made the game using Turtle,a library i found while i was watching some tutorials of FreeCodeCamp about an year ago. I've also use pygame for music background control. Pong represents a 1v1 minigame where players control a paddle with the purpose of scoring in each other opposite side. The game uses arrows and keyboard keys to control the paddles

I used a basic resolution 1920x1080p. The two paddles are colored based on my favourite colors green and blue and are represented by turtle objects The left player uses "W" and "S" keys to move the paddle and the right player uses "Up arrow" and "Down arrow" to move the paddle The ball is represented as a magenta turtle object and its moving is based on vectorial mathematics and coordinate manipulations in a while loop

I've also added a Score Board that tracks the current score of the players (Player A:x points and Player B:y points) at the top of the screen

I have included the pygame library to control and loop a favourite song of mine from when i was a little kid with the purpose of adding some nostalgia to the game and to the old times when arcade games where the main attractions

For the game logic i made a loop to constantly check and update the screen to display the game elements and check for collisons with the boundaries of the screen. When the ball touches a paddle the oppsoite player scores a point that is added up in the score board and is displayed on-spot
