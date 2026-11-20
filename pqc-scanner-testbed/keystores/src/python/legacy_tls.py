"""Legacy TLS client/server settings. TEST ONLY."""
import socket
import ssl


def tls10_client_context() -> ssl.SSLContext:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    ctx.set_ciphers("DES-CBC3-SHA:RC4-SHA")
    return ctx


def tls_min_v1_1() -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    ctx.minimum_version = ssl.TLSVersion.TLSv1_1
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def start_tls_server(port: int = 8443) -> None:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.minimum_version = ssl.TLSVersion.TLSv1
    ctx.load_cert_chain("certs/rsa_server.cert", "keys/rsa_private.pem")
    with socket.create_server(("0.0.0.0", port)) as sock:
        with ctx.wrap_socket(sock, server_side=True) as ssock:
            ssock.accept()
