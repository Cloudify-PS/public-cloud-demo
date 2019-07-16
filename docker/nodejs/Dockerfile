FROM node:lts-buster
RUN npm install http-server -g
RUN apt-get update
RUN apt-get install -y vsftpd
ADD vsftpd.conf /etc/vsftpd/vsftpd.conf
EXPOSE 8080
EXPOSE 20
EXPOSE 21
EXPOSE 10000-10100
CMD ["http-server"]
