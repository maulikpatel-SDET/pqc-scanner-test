# Dockerfile generating RSA keys and forcing legacy TLS. TEST ONLY.
FROM node:18-bullseye
RUN openssl genrsa -out /etc/ssl/private/server.key 2048 && \
    openssl req -new -x509 -sha1 -key /etc/ssl/private/server.key \
      -out /etc/ssl/certs/server.crt -days 3650 -subj "/CN=testbed.local"
RUN openssl ecparam -name prime256v1 -genkey -noout -out /etc/ssl/private/ec.key
RUN sed -i 's/MinProtocol = TLSv1.2/MinProtocol = TLSv1/' /etc/ssl/openssl.cnf && \
    sed -i 's/CipherString = DEFAULT@SECLEVEL=2/CipherString = DEFAULT@SECLEVEL=0/' /etc/ssl/openssl.cnf
ENV NODE_OPTIONS="--tls-min-v1.0 --tls-cipher-list=DES-CBC3-SHA:RC4-SHA"
ENV JWT_ALGORITHM=RS256
COPY keys/rsa_private.pem /app/keys/
CMD ["node", "server.js"]
