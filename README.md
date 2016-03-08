# shodan_ip2openports
This is a simple script that uses the Shodan.io API to get the open ports (output) of a specific IP address (input).

### Requirements:
* Create an account on Shodan.io and copy your API key;
* Install the Shodan API (python) 
  `$ sudo pip install shodan`  
  or
  `$ sudo easy_install shodan`

### Runing the script:
`python shoda_ip2openports.py <IP_address>`

### Example:
* Input:
`$ python shoda_ip2openports.py 8.8.8.8`
* Output:
`8.8.8.8;2016-03-08T15:46:27.122496;53`
* Interpretation: 
The IP address 8.8.8.8 (Known google DNS resolver) has the port 53 (DNS service) open and it was last checked at 2016-03-08T15:46:27.122496
