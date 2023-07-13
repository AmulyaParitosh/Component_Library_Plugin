from functools import cache

import certifi
from PySide6.QtCore import Slot
from PySide6.QtNetwork import (QNetworkAccessManager, QNetworkReply,
                               QNetworkRequest, QSsl, QSslCertificate,
                               QSslConfiguration, QSslSocket)

Slot(QNetworkReply)
def on_finish(reply: QNetworkReply) -> None:

    er: QNetworkReply.NetworkError = reply.error()

    if er == QNetworkReply.NetworkError.NoError:
        print(reply.url().toString(), ":", reply.attribute(QNetworkRequest.Attribute.HttpStatusCodeAttribute))

    elif er == QNetworkReply.NetworkError.ProtocolUnknownError:
        print("Blank URL passed!")

    else:
        print("Error occured: ", er)
        print(reply.url().toString(), reply.errorString())


@cache
def get_network_access_manager() -> tuple[QNetworkAccessManager, QSslConfiguration]:
    qcerts: list[QSslCertificate] = QSslCertificate.fromPath(
        certifi.where(),
        QSsl.EncodingFormat.Pem,
        QSslCertificate.PatternSyntax.Wildcard,
    )

    sslConfig: QSslConfiguration = QSslConfiguration.defaultConfiguration()
    sslConfig.setProtocol(QSsl.SslProtocol.TlsV1_0)
    sslConfig.setPeerVerifyDepth(1)
    sslConfig.setPeerVerifyMode(QSslSocket.PeerVerifyMode.VerifyPeer)
    sslConfig.setCaCertificates(qcerts)

    network_access_manager = QNetworkAccessManager()
    network_access_manager.finished.connect(on_finish)

    return network_access_manager, sslConfig
