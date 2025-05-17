def paginate(queryset, skip: int = 0, limit: int = 10):
    total = queryset.count()
    results = queryset.offset(skip).limit(limit).all()

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": results
    }
