# Django Rest Framework

## Viewsets

- `viewsets.ViewSet`
  - list()
  - create()
  - retrieve()
  - update()
  - delete()
- `viewsets.ModelViewSet` : Take only queryset and serializer_class an automatically provides both pk based and non-pk based operations.

## Pagination

**PageNumberPagination** : `/blogs/?page=10`

- page_size = 10
- Takes a page_size parameter and returns the response accordingly

**LimitOffsetPagination** : `/blogs/?limit=10&offset=0`

- **Limit** : This parameter controls how many items you want to see in a single page.
- **Offset** : This parameter tells the API where to start fetching the items from.
  - If offset = 0, you get the first 10 blogs (item 1 - 10). `blogs/?limit=10&offset=0`
  - If offset = 10, you get the next 10 blogs (item 11 - 20). `blogs/?limit=10&offset=10`
  - If offset = 90, you get the last 10 blogs (item 91 - 100). `blogs/?limit=10&offset=90`
