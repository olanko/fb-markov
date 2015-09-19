f = File.open('fswords.txt', 'r')
f.seek(0)
s = f.read

#Remove non alpanumerical characters
s = s.gsub(/[^[:alnum:] ]/, "").downcase

wds = s.split

#Delete some unneedeed words, ie. URLs
wds.delete_if { |w| w =~ /^http.*/ }

#doubles contains all possible word pairs
doubles = Hash.new

#wds.each do |w| puts "#{w}" end

#wds.each do |w| print "." end

#Find all two word pairs
for i in 0 .. wds.length - 1 do
    if wds[i] and wds[i + 1]
        if !doubles[wds[i]]
            doubles[wds[i]] = Array.[](wds[i + 1])
        else
            doubles[wds[i]].push(wds[i + 1])
        end
    end
end

#doubles.each do |d| puts "#{d}" end

#Select random seed from words
seed = wds[rand(wds.length - 1)]
s = ""

for i in 1 .. 20 do
    s += "#{seed} "
    #Fetch next seed from doubles
    seed = doubles[seed][rand(doubles[seed].length - 1)]
end

puts s
