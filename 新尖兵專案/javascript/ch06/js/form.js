var elForm = document.getElementById('formSignup');
var elSelectPackage = document.getElementById('package');
var elPackageHint = document.getElementById('packageHint');
var elTerms = document.getElementById('terms');
var elTermsHint = document.getElementById('termsHint');

elForm.addEventListener('submit',(event)=>{
    if(!elTerms.checked){
        elTermsHint.innerHTML = "必需要同意才可以發送";
        event.preventDefault();
    }
});

elSelectPackage.addEventListener('change',(event)=>{
    var target = event.target;
    var pack = target.options[target.selectedIndex].value;
    if(pack == 'monthly'){
        elPackageHint.innerHTML = "如果付一年費用，可以省$10";
    }else{
        elPackageHint.innerHTML  = "很好的選擇";
    }
});