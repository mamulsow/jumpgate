from jumpgate.common.dispatcher import Dispatcher
from jumpgate.api import app

image_dispatcher = Dispatcher(app)

# V2 API - http://api.openstack.org/api-ref-image.html#os-images-2.0

image_dispatcher.add_endpoint('v2_schema_image',
                              '/v2/schemas/image')
image_dispatcher.add_endpoint('v2_schema_images',
                              '/v2/schemas/images')
image_dispatcher.add_endpoint('v2_image',
                              '/v2/images/{image_guid}')
image_dispatcher.add_endpoint('v2_images', '/v2/images')
image_dispatcher.add_endpoint('v2_images_detail',
                              '/v2/images/detail')
image_dispatcher.add_endpoint('v2_image_file', '/v2/images/{image_guid}/file')
image_dispatcher.add_endpoint('v2_image_tag',
                              '/v2/images/{image_guid}/tags/{tag}')
image_dispatcher.add_endpoint('v2_tenant_image',
                              '/v2/{tenant_id}/images/{image_guid}')
image_dispatcher.add_endpoint('v2_tenant_images', '/v2/{tenant_id}/images')
image_dispatcher.add_endpoint('v2_tenant_images_detail',
                              '/v2/{tenant_id}/images/detail')

# V1 API - http://api.openstack.org/api-ref-image.html#os-images-1.0

image_dispatcher.add_endpoint('v1_image', '/v1/images/{image_guid}')
image_dispatcher.add_endpoint('v1_images', '/v1/images')
image_dispatcher.add_endpoint('v1_images_detail', '/v1/images/detail')
image_dispatcher.add_endpoint('v1_image_members',
                              '/v1/images/{image_guid}/members')
image_dispatcher.add_endpoint('v1_image_owner',
                              '/v1/images/{image_guid}/members/{owner}')
image_dispatcher.add_endpoint('v1_shared_image_owner',
                              '/v1/shared-images/{owner}')