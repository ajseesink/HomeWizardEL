# HomeWizardEL
HomeWizard Enegery Link

The HomeWizard Energy Link shows Electricity and Gas consumption. While I'm not a programmer wizard, I had to find out how to handle something in JSON. I have not that much knowledge of Python programming, so I had to learn that too.

In the past I did learn some Basic, Pascal, C so Python is rather new to me.

The idea is to readout the HomeWizard Energy Link (HomeWizard EL) and get a day-to-day measure of the HomeWizard EL. First step is to get these readings in a CSV format so I can read it in a spreadsheet. Second step is to get these readings in Domoticz.

Yes I know there is also the https://github.com/rvdvoorde/domoticz-homewizard, but this is not delivering what I wanted. So I decided to do some programming myself.

I added an example crontab file and a script. 
This way you can run it for example every hour.

