# update and upgrade
sudo apt update
sudo apt upgrade -y 

# neofetch
sudo apt install -y  neofetch

# gnome tweak
sudo apt install -y gnome-tweak-tool


# chrome

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb

# purge firefox

sudo apt purge firefox

#requires input

ana=$(wget -O - https://www.anaconda.com/distribution/ 2>/dev/null | sed -ne 's@.*\(https:\/\/repo\.anaconda\.com\/archive\/Anaconda3-.*-Linux-x86_64\.sh\)\">64-Bit (x86) Installer.*@\1@p')	
wget -O anaconda.sh $ana
bash anaconda.sh -b
export ANACONDA=/home/$USER/anaconda3
export PATH=$PATH:/home/$USER/anaconda3/bin
conda init
source ~/.bashrc
rm anaconda.sh

#install vscode
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"

sudo apt install code -y 

# install extensions

code --install-extension --force eamodio.gitlens
code --install-extension --force GrapeCity.gc-excelviewer
code --install-extension --force Gruntfuggly.activitusbar
code --install-extension --force Ikuyadeu.r
code --install-extension --force ms-python.python
code --install-extension --force ms-python.vscode-pylance
code --install-extension --force ms-toolsai.jupyter
code --install-extension --force ms-vscode.cpptools
code --install-extension --force Nightrains.robloxlsp
code --install-extension --force s-nlf-fh.glassit
code --install-extension --force vscodevim.vim
code --install-extension --force wraith13.zoombar-vscode
code --install-extension --force zhuangtongfa.material-theme

# change settings 

mkdir -p ~/.config/Code/User
cp Code/settings.json ~/.config/Code/User/
cp Code/keybindings.json ~/.config/Code/User/


# cloud service

sudo apt install -y libssl-dev
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

sudo apt-get install apt-transport-https ca-certificates gnupg

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

sudo apt-get update && sudo apt-get install google-cloud-sdk -y

# install autokey

sudo apt install -y autokey-gtk

# copy the config files 
mkdir -p ~/.config/autokey/data
cp -r my_scripts ~/.config/autokey/data/
cp autokey.json ~/.config/autokey/

# install fusuma 

sudo gpasswd -a $USER input
newgrp input
sudo apt install -y libinput-tools xdotool  
sudo apt install -y ruby 
sudo gem install fusuma

# config files
mkdir -p ~/.config/fusuma
cp fusuma/config.yml ~/.config/fusuma/

# install ncspot
sudo apt install -y libncursesw5-dev libdbus-1-dev libpulse-dev libssl-dev libxcb1-dev libxcb-render0-dev libxcb-shape0-dev libxcb-xfixes0-dev

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

cargo install ncspot

# setup settings 

mkdir -p ~/.config/ncspot
cp ncspot/config.toml ~/.config/ncspot/


# install tuir

pip install tuir

# install xbindkeys

sudo apt install -y xbindkeys  

cp .xbindkeysrc ~/


# r and R studio
sudo apt install -y dirmngr gnupg apt-transport-https ca-certificates software-properties-common
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'

sudo apt install -y r-base

wget -O Rstudio.deb https://download1.rstudio.org/desktop/bionic/amd64/rstudio-1.3.1093-amd64.deb

sudo apt install -y ./Rstudio.deb 

rm Rstudio.deb

# copiar la configuracion


mkdir -p ~/.config/rstudio/themes
cp rstudio/atom.rstheme ~/.config/rstudio/themes/
cp rstudio/rstudio-prefs.json ~/.config/rstudio/

# onedrive 
sudo apt install -y build-essential
sudo apt install -y libcurl4-openssl-dev
sudo apt install -y libsqlite3-dev
sudo apt install -y pkg-config
sudo apt install -y git
sudo apt install -y curl
 
curl -fsS https://dlang.org/install.sh | bash -s dmd

git clone https://github.com/abraunegg/onedrive.git

cd onedrive
./configure

make clean; make;
sudo make install
cd ..
cd ..

mkdir -p ~/.config/onedrive
cp onedrive_i/config ~/.config/onedrive/
cp onedrive_i/sync_list ~/.config/onedrive/


# devilspie2

sudo apt install -y devilspie2

cp -r devilspie2 ~/config/


# configuraciones iniciales 
cp -r autostart ~/.config/autostart

