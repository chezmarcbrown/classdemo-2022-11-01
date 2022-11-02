from django.http import JsonResponse

from .models import Comment, Listing


def api_add_comment(request, listing_id):
    c = Comment.objects.create(commenter=request.user,
                               comment=request.POST["comment_text"],
                               listing=Listing.objects.get(pk=listing_id))
    print(f'api_add_comment called. comment = {c.comment}')
    return JsonResponse({
        'comment': c.comment,
        'commenter': f'{c.commenter}',
        'created_at': c.created_at
    })
