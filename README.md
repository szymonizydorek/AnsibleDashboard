# Dashboard Project

The **Dashboard Project** is a web-based server monitoring tool that allows users to view essential server metrics in a user-friendly interface. This project includes a simple dashboard built with HTML, CSS, and a backend to monitor server resources such as CPU, RAM, disk usage, and more.

Apart from Dashboard Setup, the system also provides other useful roles to manage you infradtructure.

## Roles:
- **Docker**: This role allows to pull Jenkins image and run it as a Docker container with the usage of Exec file (systemd)
- **Security**: This role runs security audit and then make sure the system is closed and secured.
- **Linux Admin**: The dashboard adjusts to different screen sizes, making it accessible from boh desktop and mobile devices.
Apart from NGINX-based HTML, data driven server dashboard - Project involves multiple additional roles useful for any Linux admin.


## Features:
- **Server Metrics**: Displays real-time server data such as CPU usage, memory usage, disk space, and network activity.
- **Custom Styling**: The dashboard uses a clean, modern design with custom CSS, including a gradient color scheme and rounded corners.
- **Responsive Design**: The dashboard adjusts to different screen sizes, making it accessible from both desktop and mobile devices.

## Technologies Used:
- **HTML5**: For the basic structure of the dashboard.
- **CSS3**: For styling, including a gradient color scheme and responsive layout.
- **Ansible**: Used for server automation and deployment of the web dashboard.
- **Docker**: Docker role was used to manage the containerized apps such as Jenkins 
- **Jenkins**: Conteineraized application that allows building CI/CD pipelines.

## Setup:
1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
2. Run main playbook that contains all the roles:
   ```bash
   ansible-playbook main_playbook.yml --ask-vault-password
