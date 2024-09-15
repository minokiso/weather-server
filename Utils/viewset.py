import traceback
from functools import wraps

from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import GenericViewSet

from Utils.response import SuccessResponse, FailureResponse


def handle_error(name=None):
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            try:
                result = func(self, request, *args, **kwargs)
                return SuccessResponse(result.data if isinstance(result, Response) else result)
            except Exception as e:
                traceback.print_exc()
                return FailureResponse(err=str(e))

        return wrapper

    return decorator


class CreateModelMixinPlus(mixins.CreateModelMixin):
    @handle_error()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class RetrieveModelMixinPlus(mixins.RetrieveModelMixin):
    @handle_error()
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class UpdateModelMixinPlus(mixins.UpdateModelMixin):
    @handle_error()
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class DestroyModelMixinPlus(mixins.DestroyModelMixin):
    @handle_error()
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ListModelMixinPlus(mixins.ListModelMixin):
    @handle_error()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(methods=['get'], detail=False, name='no_pagination')
    @handle_error()
    def no_pagination_list(self, request, *args, **kwargs):
        self.pagination_class = []
        return super().list(request, *args, **kwargs)


class GenericViewSetPlus(GenericViewSet):
    model = None
    fields = "__all__"
    queryset = None
    serializer_class = None
    depth = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.model:
            raise ValueError("please provide a model")
        if not self.queryset:
            self.queryset = self.model.objects.all()
        if not self.serializer_class:
            class _ModelSerializer(ModelSerializer):
                class Meta:
                    model = self.model
                    fields = self.fields or "__all__"
                    depth = self.depth

            self.serializer_class = _ModelSerializer


class ModelViewSetPlus(CreateModelMixinPlus,
                       RetrieveModelMixinPlus,
                       UpdateModelMixinPlus,
                       DestroyModelMixinPlus,
                       ListModelMixinPlus,
                       GenericViewSetPlus):
    pass
