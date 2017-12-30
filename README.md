# rpi_christmas_tree_ideas

Rough scripts for PiHut's <a href="https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi">3D Xmas Tree for Raspberry Pi </a>.

tree.py is the default program given on the product's <a href="https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi">store page</a>.

tree2.py to tree5.py revolve around the basic premise of turning on or off the Xmas tree LEDs in succession (by row, randomly, etc).

tree6.py and tree7.py borrow from the Gpiozero documentation ["Who's home indicator" recipe](http://gpiozero.readthedocs.io/en/stable/recipes_advanced.html#who-s-home-indicator) to light up rows of the tree depending on whether specific devices are connected to a network, or the number of devices connected to the network, respectively.

