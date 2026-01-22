---
title: "Laravel register"
date: 2024-10-17T20:20:13-03:00
tags: ['laravel']
---
```bash  
composer require laravel/jetstream  
php artisan jetstream:install livewire  
npm install  
npm run build  
Cambios en la base de datos.  
Andá a la carpeta: database > migrations > 2014...create_users_table.php  
Y agregá el campo que quieras:  
$table->string('usertype')->default(0);  
$table->string('phone')->default(0);  
$table->string('address')->default(0);  
php artisan migrate  
```  
  
Andá a la carpeta auth al archivo register.blade.php y agregá el campo.  
  
```html  
<div class="mt-4">  
  <x-jet-label for="phone" value="{{ __('phone') }}/>  
  <x-jet-input id="phone" class="block mt-1 w-full" type="number" value="{{ __('phone') }}/>  
  <></>  
</div>  
```  
  
`config > fortify.php`  
  
```php  
'home' => '/redirect',  
```  
  
`routes > web.php`  
  
```php  
use App\Http\Controllers\HomeController;  
route::get('/redirect',[HomeController::class,'redirect']);  
```  
```bash  
php artisan make:controller HomeController`  
```  
  
`Http > Controllers > HomeController.php`  
  
```php  
<?php  
namespace App\Http\Controllers;  
  
use Illuminate\Http\Request;  
use Illuminate\Support\Facades\Auth;  
use App\Models\User;  
  
class HomeController extends Controller  
{  
    public function redirect(){  
        $usertype = Auth::user()->usertype;  
        if ($usertype == '1'){  
            return view('admin.home');  
        }  
        else  
        {  
            return view('dashboard');  
        }  
    }  
}  
?>  
```  
  
mkdir views/admin  
vim views/admin/home.blade.php  
  
```php  
<x-app-layout>  
</x-app-layout>  
```  
  
vim layouts/app.blade.php  
  
Descomprimí el template frontend en public  
  
mkdir views/User    
vim views/User/home.blade.php    
  
vim routes/web.php
route::get('/home',[HomeController::class,'index']);


`Http > Controllers > HomeController.php`  

```php
public function index()
{
    return view('User.home');
}
```
