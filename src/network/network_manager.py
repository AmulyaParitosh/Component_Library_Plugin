
# SPDX-License-Identifier: MIT
# --------------------------------------------------------------
#|																|
#|             Copyright 2023 - 2023, Amulya Paritosh			|
#|																|
#|  This file is part of Component Library Plugin for FreeCAD.	|
#|																|
#|               This file was created as a part of				|
#|              Google Summer Of Code Program - 2023			|
#|																|
# --------------------------------------------------------------

from functools import cache

import certifi
from PySide6.QtCore import Slot
from PySide6.QtNetwork import (QNetworkAccessManager, QNetworkReply,
                               QNetworkRequest, QSsl, QSslCertificate,
                               QSslConfiguration, QSslSocket)


# Slot function to handle the completion of network requests
@Slot(QNetworkReply)
def on_finish(reply: QNetworkReply) -> None:
    # Get the network error code from the reply
    er: QNetworkReply.NetworkError = reply.error()

    if er == QNetworkReply.NetworkError.NoError:
        # If there is no network error, print the URL and HTTP status code of the reply
        print(reply.url().toString(), ":", reply.attribute(QNetworkRequest.Attribute.HttpStatusCodeAttribute))

    elif er == QNetworkReply.NetworkError.ProtocolUnknownError:
        # If the network error is due to an unknown protocol, print a message indicating a blank URL
        print("Blank URL passed!")

    else:
        # If there is any other network error, print the error code and error string along with the URL
        print("Error occurred: ", er)
        print(reply.url().toString(), reply.errorString())

# Cache decorator ensures that the function result is cached for subsequent calls with the same arguments
@cache
def get_network_access_manager() -> tuple[QNetworkAccessManager, QSslConfiguration]:
    # Load the certificates from the certifi package
    qcerts: list[QSslCertificate] = QSslCertificate.fromPath(
        certifi.where(),
        QSsl.EncodingFormat.Pem,
        QSslCertificate.PatternSyntax.Wildcard,
    )

    # Create a default SSL configuration
    sslConfig: QSslConfiguration = QSslConfiguration.defaultConfiguration()
    sslConfig.setProtocol(QSsl.SslProtocol.TlsV1_0)
    sslConfig.setPeerVerifyDepth(1)
    sslConfig.setPeerVerifyMode(QSslSocket.PeerVerifyMode.VerifyPeer)
    sslConfig.setCaCertificates(qcerts)

    # Create a QNetworkAccessManager for making network requests
    network_access_manager = QNetworkAccessManager()
    network_access_manager.finished.connect(on_finish)

    return network_access_manager, sslConfig
