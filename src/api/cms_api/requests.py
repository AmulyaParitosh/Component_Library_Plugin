from PySide6.QtCore import QFile, QIODevice, QUrl, QUrlQuery
from PySide6.QtNetwork import QHttpMultiPart, QHttpPart, QNetworkRequest

from .query import RepoComponentQuery


class ComponentRequest(QNetworkRequest):
    endpoint: str = "component"

    def __init__(self, state: RepoComponentQuery | None = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setUrl(self.endpoint)
        if isinstance(state, RepoComponentQuery):
            self.from_states(state)

    def from_states(self, state: RepoComponentQuery) -> None:
        # Construct a URL query based on the provided 'RepoComponentQuery' state
        query_list: list[str] = [
            state.page,
            state.page_size,
            state.search_key,
            state.sort_by,
            state.sort_ord,
            state.file_types,
            state.tags,
            state.columns,
        ]
        query = QUrlQuery()
        query.setQuery("&".join(item for item in query_list if item))

        url: QUrl = self.url()
        url.setQuery(query)
        self.setUrl(url)


def construct_multipart(data: dict) -> QHttpMultiPart:
    multi_part = QHttpMultiPart(QHttpMultiPart.ContentType.FormDataType)

    # Append file parts to the multi-part form data
    for field, val in data.pop("files").items():
        if not isinstance(val, (list, tuple, set)):
            val = [val]
        for filepath in val:
            # TODO: Construct a file part for the multi-part form data
            multi_part.append(construct_file_part(field, filepath))

    # Append text parts to the multi-part form data
    for field, value in data.items():
        if isinstance(value, (list, tuple, set)):
            value = ','.join(value)
        # TODO: Construct a text part for the multi-part form data
        multi_part.append(construct_text_parts(field, value))

    return multi_part


def construct_text_parts(field, value):
    post_part = QHttpPart()
    post_part.setHeader(
        QNetworkRequest.KnownHeaders.ContentDispositionHeader,
        f'form-data; name=\"{field}\"',
    )
    post_part.setBody(str(value).encode())
    return post_part


def construct_file_part(field, filepath) -> QHttpPart | None:
    file = QFile(filepath)
    if not file.open(QIODevice.OpenModeFlag.ReadOnly):
        return None
    post_part = QHttpPart()
    post_part.setHeader(
        QNetworkRequest.KnownHeaders.ContentDispositionHeader,
        f'form-data; name=\"{field}\"; filename=\"{file.fileName()}\"',
    )
    post_part.setBodyDevice(file)
    return post_part
