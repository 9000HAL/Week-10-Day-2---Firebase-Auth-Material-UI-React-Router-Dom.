
//Count Characters in Your String
//The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
//What if the string is empty? Then the result should be empty object literal, {}.
//count_char('aa') => {'a': 2}
//count_char('') => {}
//count_char('aabb') => {'a': 2, 'b': 2}



function char_count (str) {
    let my_dict = {}
    my_array = str.split("")
    //console.log(my_array) ---->>see console log it works
    for (let i = 0; i < my_array.length; i++) {
        if (!my_dict[my_array[i]]) {
            //let letter = my_array[i]
            //console.leg(letter)
            my_dict[my_array[i]] = 1;
            //console.log(my_dict[my_array[i]])
        } else {
            my_dict[my_array[i]] += 1;
            //console.log(my_dict)

        }
        
    }
    return my_dict

}
 

console.log(char_count('aabb'))

//"if occurence of a letter happens more than once, add changes to value"




///USE FOR CODEWARS ABOVE !!!!!!!!!!!!!!!!!!

//----> AT END OF WEEKEND SUNDAY: MUST BE AT 200 points!!!!!!!!!!!!!!---check in with ca or dk then +100 more by thursday last day class!!!!!