from django.shortcuts import render, redirect
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def daftar(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User berhasil di buat')
            return redirect('daftar')
        else:
            messages.error(request, 'Terjadi kesalahan')
            return redirect('daftar')
    else:
        form = UserCreationForm()
        konteks = {
            'form': form,
        }
    return render(request, 'daftar.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    buku.delete()

    messages.success(request, "Data berhasil di hapus")
    return redirect('buku')


@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui")
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form': form,
            'buku': buku,
        }
    return render(request, template, konteks)


@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    books = Buku.objects.all()

    konteks = {
        'books': books,
    }

    # return HttpResponse('Halaman Buku')
    return render(request, 'buku.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    return render(request, 'penerbit.html')


@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = 'Data berhasil disimpan'

            konteks = {
                'form': form,
                'pesan': pesan
            }

            return render(request, 'tambah-buku.html', konteks)

    else:
        form = FormBuku()

        konteks = {
            'form': form
        }

        return render(request, 'tambah-buku.html', konteks)
