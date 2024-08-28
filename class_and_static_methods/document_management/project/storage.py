from class_and_static_methods.document_management.project.topic import Topic
from project.category import Category
from project.document import Document


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        self.__edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        self.__edit_object(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        self.__edit_object(document_id, self.documents, new_file_name)

    def delete_category(self, category_id: int) -> None:
        self.__delete_object(category_id, self.categories)

    def delete_topic(self, topic_id: int) -> None:
        self.__delete_object(topic_id, self.topics)

    def delete_document(self, document_id: int) -> None:
        self.__delete_object(document_id, self.documents)

    def get_document(self, document_id: int) -> None:
        return self.__find_object(document_id, self.documents)

    def __repr__(self):
        return f"\n".join([str(d) for d in self.documents])

    def __delete_object(self, object_id: int, object_collection: list):
        current_object = self.__find_object(object_id, object_collection)
        if current_object and current_object in object_collection:
            object_collection.remove(current_object)

    def __edit_object(self, object_id: int, object_collection: list, *new_values) -> None:
        current_object = self.__find_object(object_id, object_collection)
        if current_object:
            current_object.edit(*new_values)

    @staticmethod
    def __find_object(object_id, objects_collection):
        return next((o for o in objects_collection if o.id == object_id), None)
