from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Supplier, PurchaseOrder, PurchaseOrderItem
from .forms import SupplierForm, PurchaseOrderForm, PurchaseOrderItemForm
from apps.authentication.decorators import (
    admin_or_manager_or_staff_required,
    admin_required,
)
from django.forms import modelformset_factory
# =================================== supplier list view ===================================
@login_required
@admin_or_manager_or_staff_required
def supplier_list(request):
    search_query = request.GET.get("search", "")  # Get search query from GET parameters

    # If a search query exists, filter the suppliers by name or contact_name
    if search_query:
        suppliers = Supplier.objects.filter(
            name__icontains=search_query
        ) | Supplier.objects.filter(contact_name__icontains=search_query)
    else:
        suppliers = Supplier.objects.all()  # No search query, return all suppliers

    # Paginate the filtered list of suppliers
    paginator = Paginator(suppliers, 25)
    page_number = request.GET.get(
        "page"
    )  # Get the page number from the URL query parameter
    page_obj = paginator.get_page(
        page_number
    )  # Get the page object for the current page

    # Set a table title for the template context
    table_title = "Suppliers List"

    return render(
        request,
        "supplier/suppliers.html",
        {
            "page_obj": page_obj,
            "search_query": search_query,
            "table_title": table_title,  # Add table title to context
        },
    )


# =================================== supplier add view ===================================
@login_required
@admin_or_manager_or_staff_required
def supplier_add(request):
    form_title = "Add New Supplier"
    form = SupplierForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        with transaction.atomic():
            supplier = form.save()
            messages.success(
                request,
                f'Supplier "{supplier.name}" added successfully.',
                extra_tags="bg-success",
            )
            return redirect("supplier:supplier_list")

    return render(
        request, "supplier/supplier_add.html", {"form": form, "form_title": form_title}
    )


# =================================== supplier update view ===================================
@login_required
@admin_or_manager_or_staff_required
def supplier_update(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    form_title = "Update Supplier"
    form = SupplierForm(request.POST or None, instance=supplier)

    if request.method == "POST" and form.is_valid():
        with transaction.atomic():
            form.save()
            messages.success(
                request, "Supplier updated successfully!", extra_tags="bg-success"
            )
            return redirect("supplier:supplier_list")

    return render(
        request,
        "supplier/supplier_update.html",
        {"form": form, "form_title": form_title},
    )


# =================================== supplier delete view ===================================
@login_required
@admin_required
def supplier_delete(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)

    try:
        supplier.delete()
        messages.success(
            request, f"Supplier: {supplier.name} deleted!", extra_tags="bg-danger"
        )
    except Exception as e:
        messages.error(
            request, "There was an error during the deletion!", extra_tags="bg-danger"
        )
        print(e)

    return redirect("supplier:supplier_list")


# =================================== purchase_orders_list ===================================
@login_required
@admin_or_manager_or_staff_required
def purchase_orders_list(request):
    search_query = request.GET.get('search', '')
    orders = PurchaseOrder.objects.all().order_by('-order_date')

    if search_query:
        orders = orders.filter(
            Q(supplier__name__icontains=search_query) |  # Searching by supplier's name
            Q(supplier__contact_name__icontains=search_query)  # Searching by supplier's contact name
        )

    paginator = Paginator(orders, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    table_title = "Purchase Orders List"

    return render(
        request,
        'supplier/purchase_orders_list.html',
        {
            'orders': page_obj,
            'table_title': table_title,
            'page_obj': page_obj,
            'search_query': search_query,
        }
    )


# =================================== purchase_order_create ===================================
# @login_required
# @admin_or_manager_or_staff_required
# def purchase_order_add(request):
#     form_title = "Create Purchase Order"
#     form = PurchaseOrderForm(request.POST or None)

#     if request.method == "POST" and form.is_valid():
#         with transaction.atomic():
#             purchase_order = form.save()
#             messages.success(
#                 request,
#                 f'Purchase Order #{purchase_order.id} created successfully.',
#                 extra_tags="bg-success"
#             )
#             return redirect("supplier:purchase-orders-list")  # adjust to your url name

#     return render(
#         request,
#         "supplier/purchase_order_add.html",
#         {"form": form, "form_title": form_title}
#     )


def purchase_order_add(request):
    ItemFormSet = modelformset_factory(PurchaseOrderItem, form=PurchaseOrderItemForm, extra=1, can_delete=True)
    
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST)
        formset = ItemFormSet(request.POST, request.FILES)
        
        if form.is_valid() and formset.is_valid():
            purchase_order = form.save()
            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    item = form.save(commit=False)
                    item.purchase_order = purchase_order
                    item.save()
            messages.success(request, "Purchase order created successfully.")
            return redirect('supplier:purchase-orders-list')
        else:
            # Debug form errors
            messages.error(request, "Please correct the errors below.")
            print("Form errors:", form.errors)
            print("Formset errors:", formset.errors)
    else:
        form = PurchaseOrderForm()
        formset = ItemFormSet(queryset=PurchaseOrderItem.objects.none())
    
    return render(request, 'supplier/purchase_order_add.html', {
        'form': form,
        'formset': formset,
        'form_title': 'Create New Purchase Order',
    })


# =================================== purchase_order_create ===================================
@login_required
@admin_or_manager_or_staff_required
def purchase_order_update(request, purchase_order_id):
    purchase_order = get_object_or_404(PurchaseOrder, id=purchase_order_id)
    form = PurchaseOrderForm(request.POST or None, instance=purchase_order)
    form_title = "Update Purchase Order"

    if request.method == "POST" and form.is_valid():
        with transaction.atomic():
            form.save()
            messages.success(request, "Purchase Order updated successfully!", extra_tags="bg-success")
            return redirect("supplier:purchase-orders-list")

    return render(
        request,
        'supplier/purchase_order_update.html',
        {
            'purchase_order': purchase_order,
            'form': form,
            'form_title': form_title
        }
    )


# =================================== purchase_order_delete ===================================
@login_required
@admin_or_manager_or_staff_required
def purchase_order_delete(request, purchase_order_id):
    purchase_order = get_object_or_404(PurchaseOrder, id=purchase_order_id)

    if request.method == "POST":
        purchase_order.delete()
        messages.success(request, "Purchase Order deleted successfully!", extra_tags="bg-success")
        return redirect("supplier:purchase-orders-list")

    return redirect('supplier:purchase-orders-list')


# =================================== purchase_order_detail_delete ===================================
def purchase_order_detail(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk)
    items = order.items.all()  # Related PurchaseOrderItem objects
    return render(request, 'supplier/purchase_order_detail.html', {
        'order': order,
        'items': items
    })